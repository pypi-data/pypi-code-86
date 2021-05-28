# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['OrganizationDeveloperSubscriptionArgs', 'OrganizationDeveloperSubscription']

@pulumi.input_type
class OrganizationDeveloperSubscriptionArgs:
    def __init__(__self__, *,
                 developer_id: pulumi.Input[str],
                 organization_id: pulumi.Input[str],
                 apiproduct: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OrganizationDeveloperSubscription resource.
        :param pulumi.Input[str] apiproduct: Name of the API product for which the developer is purchasing a subscription.
        :param pulumi.Input[str] end_time: Time when the API product subscription ends in milliseconds since epoch.
        :param pulumi.Input[str] start_time: Time when the API product subscription starts in milliseconds since epoch.
        """
        pulumi.set(__self__, "developer_id", developer_id)
        pulumi.set(__self__, "organization_id", organization_id)
        if apiproduct is not None:
            pulumi.set(__self__, "apiproduct", apiproduct)
        if end_time is not None:
            pulumi.set(__self__, "end_time", end_time)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter(name="developerId")
    def developer_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "developer_id")

    @developer_id.setter
    def developer_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "developer_id", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter
    def apiproduct(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the API product for which the developer is purchasing a subscription.
        """
        return pulumi.get(self, "apiproduct")

    @apiproduct.setter
    def apiproduct(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "apiproduct", value)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[str]]:
        """
        Time when the API product subscription ends in milliseconds since epoch.
        """
        return pulumi.get(self, "end_time")

    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_time", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[str]]:
        """
        Time when the API product subscription starts in milliseconds since epoch.
        """
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_time", value)


class OrganizationDeveloperSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apiproduct: Optional[pulumi.Input[str]] = None,
                 developer_id: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a subscription to an API product.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] apiproduct: Name of the API product for which the developer is purchasing a subscription.
        :param pulumi.Input[str] end_time: Time when the API product subscription ends in milliseconds since epoch.
        :param pulumi.Input[str] start_time: Time when the API product subscription starts in milliseconds since epoch.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationDeveloperSubscriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a subscription to an API product.

        :param str resource_name: The name of the resource.
        :param OrganizationDeveloperSubscriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationDeveloperSubscriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apiproduct: Optional[pulumi.Input[str]] = None,
                 developer_id: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
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
            __props__ = OrganizationDeveloperSubscriptionArgs.__new__(OrganizationDeveloperSubscriptionArgs)

            __props__.__dict__["apiproduct"] = apiproduct
            if developer_id is None and not opts.urn:
                raise TypeError("Missing required property 'developer_id'")
            __props__.__dict__["developer_id"] = developer_id
            __props__.__dict__["end_time"] = end_time
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            __props__.__dict__["start_time"] = start_time
            __props__.__dict__["created_at"] = None
            __props__.__dict__["last_modified_at"] = None
            __props__.__dict__["name"] = None
        super(OrganizationDeveloperSubscription, __self__).__init__(
            'google-native:apigee/v1:OrganizationDeveloperSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationDeveloperSubscription':
        """
        Get an existing OrganizationDeveloperSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrganizationDeveloperSubscriptionArgs.__new__(OrganizationDeveloperSubscriptionArgs)

        __props__.__dict__["apiproduct"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["end_time"] = None
        __props__.__dict__["last_modified_at"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["start_time"] = None
        return OrganizationDeveloperSubscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def apiproduct(self) -> pulumi.Output[str]:
        """
        Name of the API product for which the developer is purchasing a subscription.
        """
        return pulumi.get(self, "apiproduct")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Time when the API product subscription was created in milliseconds since epoch.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[str]:
        """
        Time when the API product subscription ends in milliseconds since epoch.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[str]:
        """
        Time when the API product subscription was last modified in milliseconds since epoch.
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the API product subscription.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        Time when the API product subscription starts in milliseconds since epoch.
        """
        return pulumi.get(self, "start_time")

