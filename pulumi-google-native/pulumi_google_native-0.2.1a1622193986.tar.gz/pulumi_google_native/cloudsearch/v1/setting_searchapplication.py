# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['SettingSearchapplicationArgs', 'SettingSearchapplication']

@pulumi.input_type
class SettingSearchapplicationArgs:
    def __init__(__self__, *,
                 data_source_restrictions: Optional[pulumi.Input[Sequence[pulumi.Input['DataSourceRestrictionArgs']]]] = None,
                 default_facet_options: Optional[pulumi.Input[Sequence[pulumi.Input['FacetOptionsArgs']]]] = None,
                 default_sort_options: Optional[pulumi.Input['SortOptionsArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_audit_log: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scoring_config: Optional[pulumi.Input['ScoringConfigArgs']] = None,
                 source_config: Optional[pulumi.Input[Sequence[pulumi.Input['SourceConfigArgs']]]] = None):
        """
        The set of arguments for constructing a SettingSearchapplication resource.
        :param pulumi.Input[Sequence[pulumi.Input['DataSourceRestrictionArgs']]] data_source_restrictions: Retrictions applied to the configurations. The maximum number of elements is 10.
        :param pulumi.Input[Sequence[pulumi.Input['FacetOptionsArgs']]] default_facet_options: The default fields for returning facet results. The sources specified here also have been included in data_source_restrictions above.
        :param pulumi.Input['SortOptionsArgs'] default_sort_options: The default options for sorting the search results
        :param pulumi.Input[str] display_name: Display name of the Search Application. The maximum length is 300 characters.
        :param pulumi.Input[bool] enable_audit_log: Indicates whether audit logging is on/off for requests made for the search application in query APIs.
        :param pulumi.Input[str] name: Name of the Search Application. Format: searchapplications/{application_id}.
        :param pulumi.Input['ScoringConfigArgs'] scoring_config: Configuration for ranking results.
        :param pulumi.Input[Sequence[pulumi.Input['SourceConfigArgs']]] source_config: Configuration for a sources specified in data_source_restrictions.
        """
        if data_source_restrictions is not None:
            pulumi.set(__self__, "data_source_restrictions", data_source_restrictions)
        if default_facet_options is not None:
            pulumi.set(__self__, "default_facet_options", default_facet_options)
        if default_sort_options is not None:
            pulumi.set(__self__, "default_sort_options", default_sort_options)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if enable_audit_log is not None:
            pulumi.set(__self__, "enable_audit_log", enable_audit_log)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scoring_config is not None:
            pulumi.set(__self__, "scoring_config", scoring_config)
        if source_config is not None:
            pulumi.set(__self__, "source_config", source_config)

    @property
    @pulumi.getter(name="dataSourceRestrictions")
    def data_source_restrictions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataSourceRestrictionArgs']]]]:
        """
        Retrictions applied to the configurations. The maximum number of elements is 10.
        """
        return pulumi.get(self, "data_source_restrictions")

    @data_source_restrictions.setter
    def data_source_restrictions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataSourceRestrictionArgs']]]]):
        pulumi.set(self, "data_source_restrictions", value)

    @property
    @pulumi.getter(name="defaultFacetOptions")
    def default_facet_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FacetOptionsArgs']]]]:
        """
        The default fields for returning facet results. The sources specified here also have been included in data_source_restrictions above.
        """
        return pulumi.get(self, "default_facet_options")

    @default_facet_options.setter
    def default_facet_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FacetOptionsArgs']]]]):
        pulumi.set(self, "default_facet_options", value)

    @property
    @pulumi.getter(name="defaultSortOptions")
    def default_sort_options(self) -> Optional[pulumi.Input['SortOptionsArgs']]:
        """
        The default options for sorting the search results
        """
        return pulumi.get(self, "default_sort_options")

    @default_sort_options.setter
    def default_sort_options(self, value: Optional[pulumi.Input['SortOptionsArgs']]):
        pulumi.set(self, "default_sort_options", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the Search Application. The maximum length is 300 characters.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="enableAuditLog")
    def enable_audit_log(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether audit logging is on/off for requests made for the search application in query APIs.
        """
        return pulumi.get(self, "enable_audit_log")

    @enable_audit_log.setter
    def enable_audit_log(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_audit_log", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Search Application. Format: searchapplications/{application_id}.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="scoringConfig")
    def scoring_config(self) -> Optional[pulumi.Input['ScoringConfigArgs']]:
        """
        Configuration for ranking results.
        """
        return pulumi.get(self, "scoring_config")

    @scoring_config.setter
    def scoring_config(self, value: Optional[pulumi.Input['ScoringConfigArgs']]):
        pulumi.set(self, "scoring_config", value)

    @property
    @pulumi.getter(name="sourceConfig")
    def source_config(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SourceConfigArgs']]]]:
        """
        Configuration for a sources specified in data_source_restrictions.
        """
        return pulumi.get(self, "source_config")

    @source_config.setter
    def source_config(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SourceConfigArgs']]]]):
        pulumi.set(self, "source_config", value)


class SettingSearchapplication(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_source_restrictions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSourceRestrictionArgs']]]]] = None,
                 default_facet_options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FacetOptionsArgs']]]]] = None,
                 default_sort_options: Optional[pulumi.Input[pulumi.InputType['SortOptionsArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_audit_log: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scoring_config: Optional[pulumi.Input[pulumi.InputType['ScoringConfigArgs']]] = None,
                 source_config: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SourceConfigArgs']]]]] = None,
                 __props__=None):
        """
        Creates a search application. **Note:** This API requires an admin account to execute.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSourceRestrictionArgs']]]] data_source_restrictions: Retrictions applied to the configurations. The maximum number of elements is 10.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FacetOptionsArgs']]]] default_facet_options: The default fields for returning facet results. The sources specified here also have been included in data_source_restrictions above.
        :param pulumi.Input[pulumi.InputType['SortOptionsArgs']] default_sort_options: The default options for sorting the search results
        :param pulumi.Input[str] display_name: Display name of the Search Application. The maximum length is 300 characters.
        :param pulumi.Input[bool] enable_audit_log: Indicates whether audit logging is on/off for requests made for the search application in query APIs.
        :param pulumi.Input[str] name: Name of the Search Application. Format: searchapplications/{application_id}.
        :param pulumi.Input[pulumi.InputType['ScoringConfigArgs']] scoring_config: Configuration for ranking results.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SourceConfigArgs']]]] source_config: Configuration for a sources specified in data_source_restrictions.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SettingSearchapplicationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a search application. **Note:** This API requires an admin account to execute.

        :param str resource_name: The name of the resource.
        :param SettingSearchapplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SettingSearchapplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_source_restrictions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSourceRestrictionArgs']]]]] = None,
                 default_facet_options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FacetOptionsArgs']]]]] = None,
                 default_sort_options: Optional[pulumi.Input[pulumi.InputType['SortOptionsArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_audit_log: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scoring_config: Optional[pulumi.Input[pulumi.InputType['ScoringConfigArgs']]] = None,
                 source_config: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SourceConfigArgs']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SettingSearchapplicationArgs.__new__(SettingSearchapplicationArgs)

            __props__.__dict__["data_source_restrictions"] = data_source_restrictions
            __props__.__dict__["default_facet_options"] = default_facet_options
            __props__.__dict__["default_sort_options"] = default_sort_options
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["enable_audit_log"] = enable_audit_log
            __props__.__dict__["name"] = name
            __props__.__dict__["scoring_config"] = scoring_config
            __props__.__dict__["source_config"] = source_config
            __props__.__dict__["operation_ids"] = None
        super(SettingSearchapplication, __self__).__init__(
            'google-native:cloudsearch/v1:SettingSearchapplication',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SettingSearchapplication':
        """
        Get an existing SettingSearchapplication resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SettingSearchapplicationArgs.__new__(SettingSearchapplicationArgs)

        __props__.__dict__["data_source_restrictions"] = None
        __props__.__dict__["default_facet_options"] = None
        __props__.__dict__["default_sort_options"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["enable_audit_log"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["operation_ids"] = None
        __props__.__dict__["scoring_config"] = None
        __props__.__dict__["source_config"] = None
        return SettingSearchapplication(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataSourceRestrictions")
    def data_source_restrictions(self) -> pulumi.Output[Sequence['outputs.DataSourceRestrictionResponse']]:
        """
        Retrictions applied to the configurations. The maximum number of elements is 10.
        """
        return pulumi.get(self, "data_source_restrictions")

    @property
    @pulumi.getter(name="defaultFacetOptions")
    def default_facet_options(self) -> pulumi.Output[Sequence['outputs.FacetOptionsResponse']]:
        """
        The default fields for returning facet results. The sources specified here also have been included in data_source_restrictions above.
        """
        return pulumi.get(self, "default_facet_options")

    @property
    @pulumi.getter(name="defaultSortOptions")
    def default_sort_options(self) -> pulumi.Output['outputs.SortOptionsResponse']:
        """
        The default options for sorting the search results
        """
        return pulumi.get(self, "default_sort_options")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Display name of the Search Application. The maximum length is 300 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enableAuditLog")
    def enable_audit_log(self) -> pulumi.Output[bool]:
        """
        Indicates whether audit logging is on/off for requests made for the search application in query APIs.
        """
        return pulumi.get(self, "enable_audit_log")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Search Application. Format: searchapplications/{application_id}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationIds")
    def operation_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        IDs of the Long Running Operations (LROs) currently running for this schema. Output only field.
        """
        return pulumi.get(self, "operation_ids")

    @property
    @pulumi.getter(name="scoringConfig")
    def scoring_config(self) -> pulumi.Output['outputs.ScoringConfigResponse']:
        """
        Configuration for ranking results.
        """
        return pulumi.get(self, "scoring_config")

    @property
    @pulumi.getter(name="sourceConfig")
    def source_config(self) -> pulumi.Output[Sequence['outputs.SourceConfigResponse']]:
        """
        Configuration for a sources specified in data_source_restrictions.
        """
        return pulumi.get(self, "source_config")

