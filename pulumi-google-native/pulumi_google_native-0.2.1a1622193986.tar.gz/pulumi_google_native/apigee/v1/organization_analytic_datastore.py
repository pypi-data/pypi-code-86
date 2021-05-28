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

__all__ = ['OrganizationAnalyticDatastoreArgs', 'OrganizationAnalyticDatastore']

@pulumi.input_type
class OrganizationAnalyticDatastoreArgs:
    def __init__(__self__, *,
                 organization_id: pulumi.Input[str],
                 datastore_config: Optional[pulumi.Input['GoogleCloudApigeeV1DatastoreConfigArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 target_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OrganizationAnalyticDatastore resource.
        :param pulumi.Input['GoogleCloudApigeeV1DatastoreConfigArgs'] datastore_config: Datastore Configurations.
        :param pulumi.Input[str] display_name: Required. Display name in UI
        :param pulumi.Input[str] target_type: Destination storage type. Supported types `gcs` or `bigquery`.
        """
        pulumi.set(__self__, "organization_id", organization_id)
        if datastore_config is not None:
            pulumi.set(__self__, "datastore_config", datastore_config)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if target_type is not None:
            pulumi.set(__self__, "target_type", target_type)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="datastoreConfig")
    def datastore_config(self) -> Optional[pulumi.Input['GoogleCloudApigeeV1DatastoreConfigArgs']]:
        """
        Datastore Configurations.
        """
        return pulumi.get(self, "datastore_config")

    @datastore_config.setter
    def datastore_config(self, value: Optional[pulumi.Input['GoogleCloudApigeeV1DatastoreConfigArgs']]):
        pulumi.set(self, "datastore_config", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Display name in UI
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[pulumi.Input[str]]:
        """
        Destination storage type. Supported types `gcs` or `bigquery`.
        """
        return pulumi.get(self, "target_type")

    @target_type.setter
    def target_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_type", value)


class OrganizationAnalyticDatastore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datastore_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1DatastoreConfigArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 target_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Datastore for an org

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1DatastoreConfigArgs']] datastore_config: Datastore Configurations.
        :param pulumi.Input[str] display_name: Required. Display name in UI
        :param pulumi.Input[str] target_type: Destination storage type. Supported types `gcs` or `bigquery`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationAnalyticDatastoreArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Datastore for an org

        :param str resource_name: The name of the resource.
        :param OrganizationAnalyticDatastoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationAnalyticDatastoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datastore_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1DatastoreConfigArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 target_type: Optional[pulumi.Input[str]] = None,
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
            __props__ = OrganizationAnalyticDatastoreArgs.__new__(OrganizationAnalyticDatastoreArgs)

            __props__.__dict__["datastore_config"] = datastore_config
            __props__.__dict__["display_name"] = display_name
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            __props__.__dict__["target_type"] = target_type
            __props__.__dict__["create_time"] = None
            __props__.__dict__["last_update_time"] = None
            __props__.__dict__["org"] = None
            __props__.__dict__["self"] = None
        super(OrganizationAnalyticDatastore, __self__).__init__(
            'google-native:apigee/v1:OrganizationAnalyticDatastore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationAnalyticDatastore':
        """
        Get an existing OrganizationAnalyticDatastore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrganizationAnalyticDatastoreArgs.__new__(OrganizationAnalyticDatastoreArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["datastore_config"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["last_update_time"] = None
        __props__.__dict__["org"] = None
        __props__.__dict__["self"] = None
        __props__.__dict__["target_type"] = None
        return OrganizationAnalyticDatastore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Datastore create time, in milliseconds since the epoch of 1970-01-01T00:00:00Z
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="datastoreConfig")
    def datastore_config(self) -> pulumi.Output['outputs.GoogleCloudApigeeV1DatastoreConfigResponse']:
        """
        Datastore Configurations.
        """
        return pulumi.get(self, "datastore_config")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Required. Display name in UI
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> pulumi.Output[str]:
        """
        Datastore last update time, in milliseconds since the epoch of 1970-01-01T00:00:00Z
        """
        return pulumi.get(self, "last_update_time")

    @property
    @pulumi.getter
    def org(self) -> pulumi.Output[str]:
        """
        Organization that the datastore belongs to
        """
        return pulumi.get(self, "org")

    @property
    @pulumi.getter
    def self(self) -> pulumi.Output[str]:
        """
        Resource link of Datastore. Example: `/organizations/{org}/analytics/datastores/{uuid}`
        """
        return pulumi.get(self, "self")

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Output[str]:
        """
        Destination storage type. Supported types `gcs` or `bigquery`.
        """
        return pulumi.get(self, "target_type")

