"""
This module provides SQL query parsing functions
"""
import re
from typing import Dict, List, Optional, Tuple, Union

import sqlparse
from sqlparse.sql import Token
from sqlparse.tokens import Name, Number, Whitespace

from sql_metadata.generalizator import Generalizator
from sql_metadata.keywords_lists import (
    COLUMNS_SECTIONS,
    KEYWORDS_BEFORE_COLUMNS,
    QueryType,
    RELEVANT_KEYWORDS,
    SUBQUERY_PRECEDING_KEYWORDS,
    SUPPORTED_QUERY_TYPES,
    TABLE_ADJUSTMENT_KEYWORDS,
    WITH_ENDING_KEYWORDS,
)
from sql_metadata.token import EmptyToken, SQLToken
from sql_metadata.utils import UniqueList


class Parser:  # pylint: disable=R0902
    """
    Main class to parse sql query
    """

    def __init__(self, sql: str = "") -> None:
        self._raw_query = sql
        self._query = self._preprocess_query()
        self._query_type = None

        self._tokens = None

        self._columns = None
        self._columns_dict = None
        self._columns_aliases_names = None
        self._columns_aliases = None
        self._columns_with_tables_aliases = dict()
        self._columns_aliases_dict = None

        self._tables = None
        self._table_aliases = None

        self._with_names = None
        self._subqueries = None
        self._subqueries_names = None

        self._limit_and_offset = None

        self._values = None
        self._values_dict = None

        self._subquery_level = 0
        self._nested_level = 0
        self._parenthesis_level = 0
        self._open_parentheses = []
        self._aliases_to_check = None
        self._is_in_nested_function = False
        self._is_in_with_block = False
        self._with_columns_candidates = dict()
        self._column_aliases_max_subquery_level = dict()

        self.sqlparse_tokens = None

    @property
    def query(self) -> str:
        """
        Returns preprocessed query
        """
        return self._query.replace("\n", " ").replace("  ", " ")

    @property
    def query_type(self) -> str:
        """
        Returns type of the query.
        Currently supported queries are:
        select, insert, update, replace, create table, alter table, with + select
        """
        if self._query_type:
            return self._query_type
        if not self._tokens:
            _ = self.tokens
        if self._tokens[0].normalized in ["CREATE", "ALTER"]:
            switch = self._tokens[0].normalized + self._tokens[1].normalized
        else:
            switch = self._tokens[0].normalized
        self._query_type = SUPPORTED_QUERY_TYPES.get(switch, "UNSUPPORTED")
        if self._query_type == "UNSUPPORTED":
            raise ValueError("Not supported query type!")
        return self._query_type

    @property
    def tokens(self) -> List[SQLToken]:
        """
        Tokenizes the query
        """
        if self._tokens is not None:
            return self._tokens

        parsed = sqlparse.parse(self._query)
        tokens = []
        # handle empty queries (#12)
        if not parsed:
            return tokens

        self.sqlparse_tokens = parsed[0].tokens
        sqlparse_tokens = self._flatten_sqlparse()
        non_empty_tokens = [
            token
            for token in sqlparse_tokens
            if token.ttype is not Whitespace and token.ttype.parent is not Whitespace
        ]
        last_keyword = None
        for index, tok in enumerate(non_empty_tokens):
            token = SQLToken(
                tok=tok,
                index=index,
                subquery_level=self._subquery_level,
                last_keyword=last_keyword,
            )
            if index > 0:
                # create links between consecutive tokens
                token.previous_token = tokens[index - 1]
                tokens[index - 1].next_token = token

            if token.is_left_parenthesis:
                self._determine_opening_parenthesis_type(token=token)
            elif token.is_right_parenthesis:
                self._determine_closing_parenthesis_type(token=token)

            if tok.is_keyword and "".join(tok.normalized.split()) in RELEVANT_KEYWORDS:
                last_keyword = tok.normalized
            token.is_in_nested_function = self._is_in_nested_function
            token.parenthesis_level = self._parenthesis_level
            tokens.append(token)

        self._tokens = tokens
        # since tokens are used in all methods required parsing (so w/o generalization)
        # we set the query type here (and not in init) to allow for generalization
        # but disallow any other usage for not supported queries to avoid unexpected
        # results which are not really an error
        _ = self.query_type
        return tokens

    @property
    def columns(self) -> List[str]:
        """
        Returns the list columns this query refers to
        """
        if self._columns is not None:
            return self._columns
        columns = UniqueList()
        tables_aliases = self.tables_aliases
        subqueries_names = self.subqueries_names

        for token in self.tokens:
            # handle CREATE TABLE queries (#35)
            if token.is_name and self.query_type == QueryType.CREATE:
                # previous token is either ( or , -> indicates the column name
                if (
                    token.is_in_parenthesis
                    and token.previous_token.is_punctuation
                    and token.last_keyword_normalized == "TABLE"
                ):
                    columns.append(token.value)
                    continue

                # we're in CREATE TABLE query with the columns
                # ignore any annotations outside the parenthesis with the list of columns
                # e.g. ) CHARACTER SET utf8;
                if (
                    not token.is_in_parenthesis
                    and token.find_nearest_token("SELECT", value_attribute="normalized")
                    is EmptyToken
                ):
                    continue

            if (
                token.is_name and not token.next_token.is_dot
            ) or token.is_keyword_column_name:
                # analyze the name tokens, column names and where condition values
                if (
                    token.last_keyword_normalized in KEYWORDS_BEFORE_COLUMNS
                    and token.previous_token.normalized not in ["AS", ")"]
                    and not token.is_alias_without_as
                    and (
                        token.left_expanded not in self.columns_aliases_names
                        or token.token_is_alias_of_self_not_from_subquery(
                            aliases_levels=self._column_aliases_max_subquery_level
                        )
                    )
                ):

                    if (
                        not (
                            # aliases of sub-queries i.e.: SELECT from (...) <alias>
                            token.previous_token.is_right_parenthesis
                            and token.value in subqueries_names
                        )
                        # custom functions - they are followed by the parenthesis
                        # e.g. custom_func(...
                        and not token.next_token.is_left_parenthesis
                    ):
                        column = token.table_prefixed_column(tables_aliases)
                        self._columns_with_tables_aliases[token.left_expanded] = column
                        self._add_to_columns_subsection(
                            keyword=token.last_keyword_normalized, column=column
                        )
                        columns.append(column)
                elif (
                    token.last_keyword_normalized == "INTO"
                    and token.previous_token.is_punctuation
                ):
                    # INSERT INTO `foo` (col1, `col2`) VALUES (..)
                    column = str(token.value).strip("`")
                    self._add_to_columns_subsection(
                        keyword=token.last_keyword_normalized, column=column
                    )
                    columns.append(column)
                elif token.left_expanded in self.columns_aliases_names:
                    self._add_to_columns_aliases_subsection(token=token)
            elif (
                token.is_wildcard
                and token.last_keyword_normalized == "SELECT"
                and not token.previous_token.is_left_parenthesis
            ):
                # handle * wildcard in select part, but ignore count(*)
                column = token.table_prefixed_column(tables_aliases)
                self._columns_with_tables_aliases[token.left_expanded] = column
                self._add_to_columns_subsection(
                    keyword=token.last_keyword_normalized, column=column
                )
                columns.append(column)

        self._columns = columns
        return self._columns

    @property
    def columns_without_subqueries(self) -> List:
        """
        Returns columns without ones explicitly coming from sub-queries
        """
        columns = self.columns
        subqueries = self.subqueries_names
        return [column for column in columns if column.split(".")[0] not in subqueries]

    @property
    def columns_dict(self) -> Dict[str, List[str]]:
        """
        Returns dictionary of column names divided into section of the query in which
        given column is present.

        Sections consist of: select, where, order_by, group_by, join, insert and update
        """
        if not self._columns_dict:
            _ = self.columns
        if self.columns_aliases_dict:
            for key, value in self.columns_aliases_dict.items():
                for alias in value:
                    resolved = self._resolve_column_alias(alias)
                    if isinstance(resolved, list):
                        for res_alias in resolved:
                            self._columns_dict.setdefault(key, UniqueList()).append(
                                res_alias
                            )
                    else:
                        self._columns_dict.setdefault(key, UniqueList()).append(
                            resolved
                        )
        return self._columns_dict

    @property
    def columns_aliases(self) -> Dict:
        """
        Returns a dictionary of column aliases with columns
        """
        if self._columns_aliases is not None:
            return self._columns_aliases
        column_aliases = dict()
        _ = self.columns
        self._aliases_to_check = (
            list(self._columns_with_tables_aliases.keys())
            + self.columns_aliases_names
            + ["*"]
        )
        for token in self.tokens:
            if (
                token.value in self.columns_aliases_names
                and token.value not in column_aliases
                and not token.previous_token.is_nested_function_start
            ):
                if token.previous_token.normalized == "AS":
                    token_check = token.get_nth_previous(2)
                else:
                    token_check = token.previous_token
                if token_check.is_column_definition_end:
                    # nested subquery like select a, (select a as b from x) as column
                    start_token = token.find_nearest_token(
                        True, value_attribute="is_column_definition_start"
                    )
                    if start_token.next_token.normalized == "SELECT":
                        # we have a subquery
                        alias_token = start_token.next_token.find_nearest_token(
                            self._aliases_to_check, direction="right"
                        )
                        alias_of = self._resolve_alias_to_column(alias_token)
                    else:
                        # chain of functions or redundant parenthesis
                        alias_of = self._find_all_columns_between_tokens(
                            start_token=start_token, end_token=token
                        )
                elif token.is_in_with_columns:
                    # columns definition is to the right in subquery
                    # we are in: with with_name (<aliases>) as (subquery)
                    alias_of = self._find_column_for_with_column_alias(token)
                else:
                    # it can be one function or a chain of functions
                    # like: sum(a) + sum(b) as alias
                    # or operation on columns like: col1 + col2 as alias
                    start_token = token.find_nearest_token(
                        [",", "SELECT"], value_attribute="normalized"
                    )
                    while start_token.is_in_nested_function:
                        start_token = start_token.find_nearest_token(
                            [",", "SELECT"], value_attribute="normalized"
                        )
                    alias_of = self._find_all_columns_between_tokens(
                        start_token=start_token, end_token=token
                    )
                if token.value != alias_of:
                    # skip aliases of self, like sum(column) as column
                    column_aliases[token.left_expanded] = alias_of

        self._columns_aliases = column_aliases
        return self._columns_aliases

    @property
    def columns_aliases_dict(self) -> Dict[str, List[str]]:
        """
        Returns dictionary of column names divided into section of the query in which
        given column is present.

        Sections consist of: select, where, order_by, group_by, join, insert and update
        """
        if self._columns_aliases_dict:
            return self._columns_aliases_dict
        _ = self.columns_aliases_names
        return self._columns_aliases_dict

    @property
    def columns_aliases_names(self) -> List[str]:
        """
        Extract names of the column aliases used in query
        """
        if self._columns_aliases_names is not None:
            return self._columns_aliases_names
        column_aliases_names = UniqueList()
        with_names = self.with_names
        subqueries_names = self.subqueries_names
        for token in self.tokens:
            if (
                token.is_name
                or (token.is_keyword and token.previous_token.normalized == "AS")
            ) and not token.next_token.is_dot:
                if (
                    token.last_keyword_normalized in KEYWORDS_BEFORE_COLUMNS
                    and (
                        token.previous_token.normalized in ["AS", ")"]
                        or token.is_alias_without_as
                    )
                    or token.is_in_with_columns
                ) and token.value not in with_names + subqueries_names:
                    alias = token.left_expanded
                    column_aliases_names.append(alias)
                    current_level = self._column_aliases_max_subquery_level.setdefault(
                        alias, 0
                    )
                    if token.subquery_level > current_level:
                        self._column_aliases_max_subquery_level[
                            alias
                        ] = token.subquery_level

        self._columns_aliases_names = column_aliases_names
        return self._columns_aliases_names

    @property
    def tables(self) -> List[str]:
        """
        Return the list of tables this query refers to
        """
        if self._tables is not None:
            return self._tables
        tables = UniqueList()
        with_names = self.with_names

        for token in self.tokens:
            if (
                (token.is_name or token.is_keyword)
                and token.last_keyword_normalized in TABLE_ADJUSTMENT_KEYWORDS
                and token.previous_token.normalized not in ["AS", "WITH"]
                and token.normalized not in ["AS", "SELECT"]
            ):
                # handle CREATE TABLE queries (#35)
                # skip keyword that are withing parenthesis-wrapped list of column
                if self.query_type == QueryType.CREATE and token.is_in_parenthesis:
                    continue

                if token.next_token.is_dot:
                    pass  # part of the qualified name
                elif token.is_in_parenthesis and (
                    token.find_nearest_token("(").previous_token.value in with_names
                    or token.last_keyword_normalized == "INTO"
                ):
                    # we are in <columns> of INSERT INTO <TABLE> (<columns>)
                    # or columns of with statement: with (<columns>) as ...
                    pass
                elif token.previous_token.is_dot:
                    tables.append(token.left_expanded)  # full qualified name
                elif (
                    token.previous_token.normalized != token.last_keyword_normalized
                    and not token.previous_token.is_punctuation
                ) or token.previous_token.is_right_parenthesis:
                    # it's not a list of tables, e.g. SELECT * FROM foo, bar
                    # hence, it can be the case of alias without AS,
                    # e.g. SELECT * FROM foo bar
                    # or an alias of subquery (SELECT * FROM foo) bar
                    pass
                else:
                    table_name = str(token.value.strip("`"))
                    tables.append(table_name)

        self._tables = tables - with_names
        return self._tables

    @property
    def limit_and_offset(self) -> Optional[Tuple[int, int]]:
        """
        Returns value for limit and offset if set
        """
        if self._limit_and_offset is not None:
            return self._limit_and_offset
        limit = None
        offset = None

        for token in self.tokens:
            if token.is_integer:
                if token.last_keyword_normalized == "LIMIT" and not limit:
                    # LIMIT <limit>
                    limit = int(token.value)
                elif token.last_keyword_normalized == "OFFSET":
                    # OFFSET <offset>
                    offset = int(token.value)
                elif token.previous_token.is_punctuation:
                    # LIMIT <offset>,<limit>
                    offset = limit
                    limit = int(token.value)

        if limit is None:
            return None

        self._limit_and_offset = limit, offset or 0
        return self._limit_and_offset

    @property
    def tables_aliases(self) -> Dict[str, str]:
        """
        Returns tables aliases mapping from a given query

        E.g. SELECT a.* FROM users1 AS a JOIN users2 AS b ON a.ip_address = b.ip_address
        will give you {'a': 'users1', 'b': 'users2'}
        """
        if self._table_aliases is not None:
            return self._table_aliases
        aliases = dict()
        tables = self.tables

        for token in self.tokens:
            if (
                token.last_keyword_normalized in TABLE_ADJUSTMENT_KEYWORDS
                and token.is_name
                and token.next_token.normalized != "AS"
                and not token.next_token.is_dot
            ):
                if token.previous_token.normalized == "AS":
                    # potential <DB.<SCHEMA>.<TABLE> as <ALIAS>
                    potential_table_name = token.get_nth_previous(2).left_expanded
                else:
                    # potential <DB.<SCHEMA>.<TABLE> <ALIAS>
                    potential_table_name = token.previous_token.left_expanded

                if potential_table_name in tables:
                    aliases[token.value] = potential_table_name

        self._table_aliases = aliases
        return self._table_aliases

    @property
    def with_names(self) -> List[str]:
        """
        Returns with statements aliases list from a given query

        E.g. WITH database1.tableFromWith AS (SELECT * FROM table3)
             SELECT "xxxxx" FROM database1.tableFromWith alias
             LEFT JOIN database2.table2 ON ("tt"."ttt"."fff" = "xx"."xxx")
        will return ["database1.tableFromWith"]
        """
        if self._with_names is not None:
            return self._with_names
        with_names = UniqueList()
        for token in self.tokens:
            if token.previous_token.normalized == "WITH":
                self._is_in_with_block = True
                while self._is_in_with_block and token.next_token:
                    # name is first
                    if token.next_token.normalized == "AS":
                        if token.is_right_parenthesis:
                            # inside columns of with statement
                            # like: with (col1, col2) as (subquery)
                            token.is_with_columns_end = True
                            token.is_nested_function_end = False
                            start_token = token.find_nearest_token("(")
                            start_token.is_with_columns_start = True
                            start_token.is_nested_function_start = False
                            prev_token = start_token.previous_token
                            with_names.append(prev_token.left_expanded)
                        else:
                            with_names.append(token.left_expanded)
                        # move to next with if exists, this with ends with
                        #  ) + , if many withs or ) + SELECT if one
                        # need to move to next as AS can be in
                        # sub-queries inside with definition
                        while token.next_token and not (
                            token.is_right_parenthesis
                            and (
                                token.next_token.is_punctuation
                                or token.next_token.normalized in WITH_ENDING_KEYWORDS
                            )
                        ):
                            token = token.next_token
                        if token.next_token.normalized in WITH_ENDING_KEYWORDS:
                            self._is_in_with_block = False
                    else:
                        token = token.next_token

        self._with_names = with_names
        return self._with_names

    @property
    def subqueries(self) -> Dict:
        """
        Returns a dictionary with all sub-queries existing in query
        """
        if self._subqueries is not None:
            return self._subqueries
        subqueries = dict()
        token = self.tokens[0]
        while token.next_token:
            if token.previous_token.is_subquery_start:
                current_subquery = []
                current_level = token.subquery_level
                inner_token = token
                while (
                    inner_token.next_token
                    and not inner_token.next_token.subquery_level < current_level
                ):
                    current_subquery.append(inner_token)
                    inner_token = inner_token.next_token
                if inner_token.next_token.value in self.subqueries_names:
                    query_name = inner_token.next_token.value
                else:
                    query_name = inner_token.next_token.next_token.value
                subquery_text = "".join([x.stringified_token for x in current_subquery])
                subqueries[query_name] = subquery_text

            token = token.next_token

        self._subqueries = subqueries
        return self._subqueries

    @property
    def subqueries_names(self) -> List[str]:
        """
        Returns sub-queries aliases list from a given query

        e.g. SELECT COUNT(1) FROM
            (SELECT std.task_id FROM some_task_detail std WHERE std.STATUS = 1) a
             JOIN (SELECT st.task_id FROM some_task st WHERE task_type_id = 80) b
             ON a.task_id = b.task_id;
        will return ["a", "b"]
        """
        if self._subqueries_names is not None:
            return self._subqueries_names
        subqueries_names = UniqueList()
        for token in self.tokens:
            if (token.previous_token.is_subquery_end and token.normalized != "AS") or (
                token.previous_token.normalized == "AS"
                and token.get_nth_previous(2).is_subquery_end
            ):
                subqueries_names.append(str(token))

        self._subqueries_names = subqueries_names
        return self._subqueries_names

    @property
    def values(self) -> List:
        """
        Returns list of values from insert queries
        """
        if self._values:
            return self._values
        values = []
        for token in self.tokens:
            if (
                token.last_keyword_normalized == "VALUES"
                and token.is_in_parenthesis
                and token.next_token.is_punctuation
            ):
                if token.is_integer:
                    value = int(token.value)
                elif token.is_float:
                    value = float(token.value)
                else:
                    value = token.value.strip("'\"")
                values.append(value)
        self._values = values
        return self._values

    @property
    def values_dict(self) -> Dict:
        """
        Returns dictionary of column-value pairs.
        If columns are not set the auto generated column_<col_number> are added.
        """
        values = self.values
        if self._values_dict or not values:
            return self._values_dict
        columns = self.columns
        if not columns:
            columns = [f"column_{ind + 1}" for ind in range(len(values))]
        values_dict = dict(zip(columns, values))
        self._values_dict = values_dict
        return self._values_dict

    @property
    def comments(self) -> List[str]:
        """
        Return comments from SQL query
        """
        return [x.value for x in self.tokens if x.is_comment]

    @property
    def without_comments(self) -> str:
        """
        Removes comments from SQL query
        """
        return Generalizator(self.query).without_comments

    @property
    def generalize(self) -> str:
        """
        Removes most variables from an SQL query
        and replaces them with X or N for numbers.

        Based on Mediawiki's DatabaseBase::generalizeSQL
        """
        return Generalizator(self._raw_query).generalize

    def _add_to_columns_subsection(self, keyword: str, column: str):
        """
        Add columns to the section in which it appears in query
        """
        section = COLUMNS_SECTIONS[keyword]
        self._columns_dict = self._columns_dict or dict()
        self._columns_dict.setdefault(section, UniqueList()).append(column)

    def _add_to_columns_aliases_subsection(self, token: SQLToken):
        """
        Add alias to the section in which it appears in query
        """
        keyword = token.last_keyword_normalized
        alias = token.left_expanded
        if (
            token.last_keyword_normalized in ["FROM", "WITH"]
            and token.find_nearest_token("(").is_with_columns_start
        ):
            keyword = "SELECT"
        section = COLUMNS_SECTIONS[keyword]
        self._columns_aliases_dict = self._columns_aliases_dict or dict()
        self._columns_aliases_dict.setdefault(section, UniqueList()).append(alias)

    def _resolve_column_alias(self, alias: str) -> str:
        """
        Returns a column name for a given alias
        """
        while alias in self.columns_aliases:
            alias = self.columns_aliases[alias]
            if isinstance(alias, list):
                break
        if isinstance(alias, list):
            alias = [self._resolve_column_alias(x) for x in alias]
        return alias

    def _resolve_alias_to_column(self, alias_token: SQLToken) -> str:
        """
        Resolves aliases of tables to already resolved columns
        """
        if alias_token.left_expanded in self._columns_with_tables_aliases:
            alias_of = self._columns_with_tables_aliases[alias_token.left_expanded]
        else:
            alias_of = alias_token.left_expanded
        return alias_of

    def _determine_opening_parenthesis_type(self, token: SQLToken):
        """
        Determines the type of left parenthesis in query
        """
        if token.previous_token.normalized in SUBQUERY_PRECEDING_KEYWORDS:
            # inside subquery / derived table
            token.is_subquery_start = True
            self._subquery_level += 1
            token.subquery_level = self._subquery_level
        elif token.previous_token.normalized in KEYWORDS_BEFORE_COLUMNS.union({","}):
            # we are in columns and in a column subquery definition
            token.is_column_definition_start = True
        elif token.previous_token.normalized == "AS":
            token.is_with_query_start = True
        else:
            # nested function
            token.is_nested_function_start = True
            self._nested_level += 1
            self._is_in_nested_function = True
        self._open_parentheses.append(token)
        self._parenthesis_level += 1

    def _determine_closing_parenthesis_type(self, token: SQLToken):
        """
        Determines the type of right parenthesis in query
        """
        last_open_parenthesis = self._open_parentheses.pop(-1)
        if last_open_parenthesis.is_subquery_start:
            token.is_subquery_end = True
            self._subquery_level -= 1
        elif last_open_parenthesis.is_column_definition_start:
            token.is_column_definition_end = True
        elif last_open_parenthesis.is_with_query_start:
            token.is_with_query_end = True
        else:
            token.is_nested_function_end = True
            self._nested_level -= 1
            if self._nested_level == 0:
                self._is_in_nested_function = False
        self._parenthesis_level -= 1

    def _find_column_for_with_column_alias(self, token: SQLToken) -> str:
        start_token = token.find_nearest_token(
            True, direction="right", value_attribute="is_with_query_start"
        )
        if start_token not in self._with_columns_candidates:
            end_token = start_token.find_nearest_token(
                True, direction="right", value_attribute="is_with_query_end"
            )
            columns = self._find_all_columns_between_tokens(
                start_token=start_token, end_token=end_token
            )
            self._with_columns_candidates[start_token] = columns
        if isinstance(self._with_columns_candidates[start_token], list):
            alias_of = self._with_columns_candidates[start_token].pop(0)
        else:
            alias_of = self._with_columns_candidates[start_token]
        return alias_of

    def _find_all_columns_between_tokens(
        self, start_token: SQLToken, end_token: SQLToken
    ) -> Union[str, List[str]]:
        """
        Returns a list of columns between two tokens
        """
        loop_token = start_token
        aliases = UniqueList()
        while loop_token.next_token != end_token:
            if loop_token.next_token.left_expanded in self._aliases_to_check:
                alias_token = loop_token.next_token
                aliases.append(self._resolve_alias_to_column(alias_token))
            loop_token = loop_token.next_token
        return aliases[0] if len(aliases) == 1 else aliases

    def _preprocess_query(self) -> str:
        """
        Perform initial query cleanup
        """
        if self._raw_query == "":
            return ""

        # python re does not have variable length look back/forward
        # so we need to replace all the " (double quote) for a
        # temporary placeholder as we DO NOT want to replace those
        # in the strings as this is something that user provided
        def replace_quotes_in_string(match):
            return re.sub('"', "<!!__QUOTE__!!>", match.group())

        def replace_back_quotes_in_string(match):
            return re.sub("<!!__QUOTE__!!>", '"', match.group())

        # unify quoting in queries, replace double quotes to backticks
        # it's best to keep the quotes as they can have keywords
        # or digits at the beginning so we only strip them in SQLToken
        # as double quotes are not properly handled in sqlparse
        query = re.sub(r"'.*?'", replace_quotes_in_string, self._raw_query)
        query = re.sub(r'"([^`]+?)"', r"`\1`", query)
        query = re.sub(r'"([^`]+?)"\."([^`]+?)"', r"`\1`.`\2`", query)
        query = re.sub(r"'.*?'", replace_back_quotes_in_string, query)

        return query

    def _flatten_sqlparse(self):
        for token in self.sqlparse_tokens:
            # sqlparse returns mysql digit starting identifiers as group
            # check https://github.com/andialbrecht/sqlparse/issues/337
            is_grouped_mysql_digit_name = (
                token.is_group
                and len(token.tokens) == 2
                and token.tokens[0].ttype is Number.Integer
                and (
                    token.tokens[1].is_group and token.tokens[1].tokens[0].ttype is Name
                )
            )
            if token.is_group and not is_grouped_mysql_digit_name:
                yield from token.flatten()
            elif is_grouped_mysql_digit_name:
                # we have digit starting name
                new_tok = Token(
                    value=f"{token.tokens[0].normalized}"
                    f"{token.tokens[1].tokens[0].normalized}",
                    ttype=token.tokens[1].tokens[0].ttype,
                )
                new_tok.parent = token.parent
                yield new_tok
                if len(token.tokens[1].tokens) > 1:
                    # unfortunately there might be nested groups
                    remaining_tokens = token.tokens[1].tokens[1:]
                    for tok in remaining_tokens:
                        if tok.is_group:
                            yield from tok.flatten()
                        else:
                            yield tok
            else:
                yield token
