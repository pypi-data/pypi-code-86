import collections
import copy
import os
import re

import pandas as pd
from numpy.random import default_rng

from .date_expressions import (
    evaluate_date_expressions_in_covariate_definitions,
    evaluate_date_expressions_in_expectations_definition,
    validate_date,
)
from .expectation_generators import generate
from .pandas_utils import dataframe_to_file
from .process_covariate_definitions import process_covariate_definitions


class StudyDefinition:

    backend = None

    def __init__(
        self, population, default_expectations=None, index_date=None, **covariates
    ):
        covariates["population"] = population
        self._original_covariates = process_covariate_definitions(covariates)
        self._original_default_expectations = default_expectations or {}
        self.set_index_date(index_date)
        self.pandas_csv_args = self.get_pandas_csv_args(self.covariate_definitions)
        self.database_url = os.environ.get("DATABASE_URL")
        self.temporary_database = os.environ.get("TEMP_DATABASE_NAME")
        if self.database_url:
            self.backend = self.create_backend()
        else:
            # Without a backend defined we can still generate dummy data but we
            # can't rely on the backend to validate the study definition for us
            self.validate_study_definition()
            self.backend = None

    def set_index_date(self, index_date):
        """
        Re-evaluate all date expressions in the covariate definitions and the
        default expecations using the supplied index date and re-initialise the
        backend with the new values
        """
        if index_date is not None:
            validate_date(index_date)
        self.index_date = index_date
        self.covariate_definitions = evaluate_date_expressions_in_covariate_definitions(
            self._original_covariates, self.index_date
        )
        self.default_expectations = (
            evaluate_date_expressions_in_expectations_definition(
                self._original_default_expectations, self.index_date
            )
        )
        if self.backend:
            self.recreate_backend()

    def to_file(self, filename, expectations_population=False, **kwargs):
        if expectations_population:
            df = self.make_df_from_expectations(expectations_population)
            # Add a patient ID - a randomly generated integer from an
            # array 10x larger than the cohort.
            df["patient_id"] = default_rng().choice(
                (len(df) * 10), size=len(df), replace=False
            )
            dataframe_to_file(df, filename)
        else:
            self.assert_backend_is_configured()
            self.backend.to_file(filename, **kwargs)

    def csv_to_df(self, csv_name):
        return pd.read_csv(
            csv_name,
            dtype=self.pandas_csv_args["dtype"],
            converters=self.pandas_csv_args["converters"],
            parse_dates=self.pandas_csv_args["parse_dates"],
        )

    def to_sql(self):
        self.assert_backend_is_configured()
        return self.backend.to_sql()

    def to_dicts(self):
        self.assert_backend_is_configured()
        return self.backend.to_dicts()

    def to_data(self):
        hidden_columns = []
        covariate_definitions = copy.deepcopy(self.covariate_definitions)
        for name, (query_type, query_args) in covariate_definitions.items():
            if query_args.pop("hidden", False):
                hidden_columns.append(name)
        data = {"hidden_columns": hidden_columns, "covariate_definitions": {}}
        for name, (query_type, query_args) in covariate_definitions.items():
            data["covariate_definitions"][name] = {
                "type": query_type,
                "args": query_args,
            }
        return data

    # ************************************************************************
    # END OF PUBLIC API
    # ************************************************************************

    @staticmethod
    def get_backend_for_database_url(database_url):
        if database_url.startswith("mssql://") or database_url.startswith(
            "mssql+pyodbc://"
        ):
            from .tpp_backend import TPPBackend

            return TPPBackend
        elif database_url.startswith("presto://"):
            from .emis_backend import EMISBackend

            return EMISBackend
        else:
            raise ValueError(f"No matching backend found for {database_url}")

    def assert_backend_is_configured(self):
        if not self.backend:
            raise RuntimeError(
                "Cannot extract data as no DATABASE_URL environment variable defined"
            )

    def validate_study_definition(self):
        # As a crude way of error checking we construct a TPP backend with a
        # dummy database URL. We immediately discard the backend instance, but
        # the process of constructing it should trigger any problems with the
        # study definition.
        self.create_backend("mssql://localhost/dummy")

    def create_backend(self, database_url=None):
        # Creates an appropriate backend for the database URL. Uses
        # the provided URL or `self.database_url` if none is provided.
        Backend = self.get_backend_for_database_url(database_url or self.database_url)
        return Backend(
            self.database_url,
            self.covariate_definitions,
            temporary_database=self.temporary_database,
        )

    def recreate_backend(self):
        self.backend.close()
        self.backend = self.create_backend()

    @staticmethod
    def get_pandas_csv_args(covariate_definitions):
        def tobool(val):
            if val == "":
                return False
            if val == "0":
                return False
            return True

        def add_month_and_day_to_date(val):
            if val:
                return val + "-01-01"
            return val

        def add_day_to_date(val):
            if val:
                return val + "-01"
            return val

        dtypes = {}
        parse_dates = []
        converters = {}
        args = {}
        date_col_for = {}

        for name, (funcname, kwargs) in covariate_definitions.items():
            if name == "population" or kwargs.get("hidden"):
                continue
            args[name] = kwargs.copy()
            column_type = kwargs["column_type"]

            # Awkward workaround: IMD is in fact an int, but it comes to us
            # rounded to nearest hundred which makes it act a bit more like a
            # categorical variable for the purposes of dummy data generation so
            # we pretend that's what it is here. Similarly, rural/urban
            # classification is as int in datatype terms but is conceptually
            # categorical, so possibly we need a categorical int type to handle
            # these.
            if kwargs.get("returning") in (
                "index_of_multiple_deprivation",
                "rural_urban_classification",
            ):
                dtypes[name] = "category"
                continue

            if column_type == "date":
                parse_dates.append(name)
                # if granularity doesn't include a day, add one
                if kwargs.get("date_format") in ("YYYY", None):
                    converters[name] = add_month_and_day_to_date
                elif kwargs.get("date_format") == "YYYY-MM":
                    converters[name] = add_day_to_date
                if funcname == "value_from":
                    date_col_for[kwargs["source"]] = name
            elif column_type == "bool":
                converters[name] = tobool
                dtypes[name] = "bool"
            elif column_type == "int":
                dtypes[name] = "Int64"
            elif column_type == "str":
                dtypes[name] = "category"
            elif column_type == "float":
                dtypes[name] = "float"
            else:
                raise ValueError(
                    f"Unable to impute Pandas type for {column_type} "
                    f"({name}: {funcname})"
                )
        return {
            "dtype": dtypes,
            "converters": converters,
            "parse_dates": parse_dates,
            "args": args,
            "date_col_for": date_col_for,
        }

    def make_df_from_expectations(self, population):
        df = pd.DataFrame()

        # Start with dates, so we can use them as inputs for incidence
        # matching on dependent columns
        for colname in self.pandas_csv_args["parse_dates"]:
            definition_args = self.pandas_csv_args["args"][colname]
            if "source" in definition_args:
                source_args = self.pandas_csv_args["args"][definition_args["source"]]
                definition_args["return_expectations"] = source_args[
                    "return_expectations"
                ]
            return_expectations = definition_args["return_expectations"] or {}
            if not self.default_expectations and not return_expectations:
                raise ValueError(
                    f"No `return_expectations` defined for {colname} "
                    "and no `default_expectations` defined for the study"
                )
            kwargs = self.default_expectations.copy()
            kwargs = merge(kwargs, return_expectations)
            self.check_date_expectations_defined(colname, kwargs)
            df[colname] = generate(population, **kwargs)["date"]

            # Now apply any date-based filtering specified in the study
            # definition
            filtered_dates = self.apply_date_filters_from_definition(
                df[colname], **definition_args
            )
            df.loc[~df.index.isin(filtered_dates.index), colname] = None

        # Now we can optionally pass in an array which has already had
        # its incidence calculated as a mask
        for colname, dtype in self.pandas_csv_args["dtype"].items():
            definition_args = self.pandas_csv_args["args"][colname]
            return_expectations = definition_args["return_expectations"] or {}
            if not self.default_expectations and not return_expectations:
                raise ValueError(
                    f"No `return_expectations` defined for {colname} "
                    "and no `default_expectations` defined for the study"
                )
            kwargs = self.default_expectations.copy()
            kwargs = merge(kwargs, return_expectations)
            self.check_date_expectations_defined(colname, kwargs)

            if dtype == "category":
                self.validate_category_expectations(
                    **self.pandas_csv_args["args"][colname]
                )

            if dtype == "bool" and "bool" not in kwargs:
                kwargs["bool"] = True

            dependent_date = self.pandas_csv_args["date_col_for"].get(colname)
            if dependent_date:
                generated_df = generate(
                    population, match_incidence=df[dependent_date], **kwargs
                )
            else:
                generated_df = generate(population, **kwargs)
            try:
                if dtype == "Int64":
                    # When defining expectations, the more
                    # user-friendly `int` is used
                    dtype = "int"
                df[colname] = generated_df[dtype]
            except KeyError:

                raise ValueError(
                    f"Column definition {colname} does not return expected type {dtype}"
                )
        # Finally, reduce date columns to the precision requested in
        # the definition
        for colname in self.pandas_csv_args["parse_dates"]:
            definition_args = self.pandas_csv_args["args"][colname]
            df[colname] = self.apply_date_precision_from_definition(
                df[colname], **definition_args
            )
        return df

    def validate_category_expectations(
        self,
        codelist=None,
        return_expectations=None,
        category_definitions=None,
        **kwargs,
    ):
        defined = set(return_expectations["category"]["ratios"].keys())
        if category_definitions:
            available = set(category_definitions.keys())
        elif codelist and codelist.has_categories:
            available = set([x[1] for x in codelist])
        else:
            available = defined
        if not defined.issubset(available):
            raise ValueError(
                f"Expected categories {', '.join(defined)} are not a subset of "
                f"available categories {', '.join(available)}"
            )

    def apply_date_filters_from_definition(self, series, between=None, **kwargs):
        min_date, max_date = self.filter_date_range(between)
        if min_date and max_date:
            series = series[(series >= min_date) & (series <= max_date)]
        elif min_date:
            series = series[series >= min_date]
        elif max_date:
            series = series[series <= max_date]
        return series

    @staticmethod
    def filter_date_range(between):
        if not between:
            return None, None
        # Filter out "dynamic" date expressions (i.e. date expressions which
        # refer to the values of other columns). Date expressions which can be
        # evaluated statically will already have been converted to ISO dates at
        # this point.  Eventually we want to support evaluating dynamic date
        # expressions here, but for now we just ignore them.
        return [
            value
            if not isinstance(value, str) or re.match(r"\d\d\d\d-\d\d-\d\d", value)
            else None
            for value in between
        ]

    def apply_date_precision_from_definition(self, series, date_format=None, **kwargs):
        if date_format == "YYYY-MM-DD":
            series = series.dt.strftime("%Y-%m-%d")
        elif date_format == "YYYY-MM":
            series = series.dt.strftime("%Y-%m")
        else:
            series = series.dt.strftime("%Y")
        return series

    def check_date_expectations_defined(self, colname, kwargs):
        if "date" not in kwargs:
            raise ValueError(f"{colname} must define a date expectation")
        for k in ["earliest", "latest"]:
            if k not in kwargs["date"]:
                raise ValueError(f"{colname} must define a date[{k}] expectation")


def merge(dict1, dict2):
    """ Return a new dictionary by merging two dictionaries recursively. """

    result = copy.deepcopy(dict1)

    for key, value in dict2.items():
        if isinstance(value, collections.abc.Mapping):
            result[key] = merge(result.get(key, {}), value)
        else:
            result[key] = copy.deepcopy(dict2[key])
    return result
