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

__all__ = ['OrganizationEnvironmentTargetserverArgs', 'OrganizationEnvironmentTargetserver']

@pulumi.input_type
class OrganizationEnvironmentTargetserverArgs:
    def __init__(__self__, *,
                 environment_id: pulumi.Input[str],
                 organization_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 s_sl_info: Optional[pulumi.Input['GoogleCloudApigeeV1TlsInfoArgs']] = None):
        """
        The set of arguments for constructing a OrganizationEnvironmentTargetserver resource.
        :param pulumi.Input[str] description: Optional. A human-readable description of this TargetServer.
        :param pulumi.Input[str] host: Required. The host name this target connects to. Value must be a valid hostname as described by RFC-1123.
        :param pulumi.Input[bool] is_enabled: Optional. Enabling/disabling a TargetServer is useful when TargetServers are used in load balancing configurations, and one or more TargetServers need to taken out of rotation periodically. Defaults to true.
        :param pulumi.Input[str] name: Required. The resource id of this target server. Values must match the regular expression 
        :param pulumi.Input[int] port: Required. The port number this target connects to on the given host. Value must be between 1 and 65535, inclusive.
        :param pulumi.Input['GoogleCloudApigeeV1TlsInfoArgs'] s_sl_info: Optional. Specifies TLS configuration info for this TargetServer. The JSON name is `sSLInfo` for legacy/backwards compatibility reasons -- Edge originally supported SSL, and the name is still used for TLS configuration.
        """
        pulumi.set(__self__, "environment_id", environment_id)
        pulumi.set(__self__, "organization_id", organization_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if is_enabled is not None:
            pulumi.set(__self__, "is_enabled", is_enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if s_sl_info is not None:
            pulumi.set(__self__, "s_sl_info", s_sl_info)

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "environment_id")

    @environment_id.setter
    def environment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_id", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. A human-readable description of this TargetServer.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The host name this target connects to. Value must be a valid hostname as described by RFC-1123.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Optional. Enabling/disabling a TargetServer is useful when TargetServers are used in load balancing configurations, and one or more TargetServers need to taken out of rotation periodically. Defaults to true.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The resource id of this target server. Values must match the regular expression 
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        Required. The port number this target connects to on the given host. Value must be between 1 and 65535, inclusive.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="sSLInfo")
    def s_sl_info(self) -> Optional[pulumi.Input['GoogleCloudApigeeV1TlsInfoArgs']]:
        """
        Optional. Specifies TLS configuration info for this TargetServer. The JSON name is `sSLInfo` for legacy/backwards compatibility reasons -- Edge originally supported SSL, and the name is still used for TLS configuration.
        """
        return pulumi.get(self, "s_sl_info")

    @s_sl_info.setter
    def s_sl_info(self, value: Optional[pulumi.Input['GoogleCloudApigeeV1TlsInfoArgs']]):
        pulumi.set(self, "s_sl_info", value)


class OrganizationEnvironmentTargetserver(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 s_sl_info: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1TlsInfoArgs']]] = None,
                 __props__=None):
        """
        Creates a TargetServer in the specified environment.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Optional. A human-readable description of this TargetServer.
        :param pulumi.Input[str] host: Required. The host name this target connects to. Value must be a valid hostname as described by RFC-1123.
        :param pulumi.Input[bool] is_enabled: Optional. Enabling/disabling a TargetServer is useful when TargetServers are used in load balancing configurations, and one or more TargetServers need to taken out of rotation periodically. Defaults to true.
        :param pulumi.Input[str] name: Required. The resource id of this target server. Values must match the regular expression 
        :param pulumi.Input[int] port: Required. The port number this target connects to on the given host. Value must be between 1 and 65535, inclusive.
        :param pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1TlsInfoArgs']] s_sl_info: Optional. Specifies TLS configuration info for this TargetServer. The JSON name is `sSLInfo` for legacy/backwards compatibility reasons -- Edge originally supported SSL, and the name is still used for TLS configuration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationEnvironmentTargetserverArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a TargetServer in the specified environment.

        :param str resource_name: The name of the resource.
        :param OrganizationEnvironmentTargetserverArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationEnvironmentTargetserverArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 s_sl_info: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1TlsInfoArgs']]] = None,
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
            __props__ = OrganizationEnvironmentTargetserverArgs.__new__(OrganizationEnvironmentTargetserverArgs)

            __props__.__dict__["description"] = description
            if environment_id is None and not opts.urn:
                raise TypeError("Missing required property 'environment_id'")
            __props__.__dict__["environment_id"] = environment_id
            __props__.__dict__["host"] = host
            __props__.__dict__["is_enabled"] = is_enabled
            __props__.__dict__["name"] = name
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            __props__.__dict__["port"] = port
            __props__.__dict__["s_sl_info"] = s_sl_info
        super(OrganizationEnvironmentTargetserver, __self__).__init__(
            'google-native:apigee/v1:OrganizationEnvironmentTargetserver',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationEnvironmentTargetserver':
        """
        Get an existing OrganizationEnvironmentTargetserver resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrganizationEnvironmentTargetserverArgs.__new__(OrganizationEnvironmentTargetserverArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["host"] = None
        __props__.__dict__["is_enabled"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["port"] = None
        __props__.__dict__["s_sl_info"] = None
        return OrganizationEnvironmentTargetserver(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. A human-readable description of this TargetServer.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[str]:
        """
        Required. The host name this target connects to. Value must be a valid hostname as described by RFC-1123.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[bool]:
        """
        Optional. Enabling/disabling a TargetServer is useful when TargetServers are used in load balancing configurations, and one or more TargetServers need to taken out of rotation periodically. Defaults to true.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required. The resource id of this target server. Values must match the regular expression 
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        Required. The port number this target connects to on the given host. Value must be between 1 and 65535, inclusive.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="sSLInfo")
    def s_sl_info(self) -> pulumi.Output['outputs.GoogleCloudApigeeV1TlsInfoResponse']:
        """
        Optional. Specifies TLS configuration info for this TargetServer. The JSON name is `sSLInfo` for legacy/backwards compatibility reasons -- Edge originally supported SSL, and the name is still used for TLS configuration.
        """
        return pulumi.get(self, "s_sl_info")

