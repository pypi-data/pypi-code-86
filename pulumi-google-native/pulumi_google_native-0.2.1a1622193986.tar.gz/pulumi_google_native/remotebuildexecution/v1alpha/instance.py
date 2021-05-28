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

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 project: pulumi.Input[str],
                 feature_policy: Optional[pulumi.Input['GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyArgs']] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logging_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input['GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyArgs'] feature_policy: The policy to define whether or not RBE features can be used or how they can be used.
        :param pulumi.Input[str] instance_id: ID of the created instance. A valid `instance_id` must: be 6-50 characters long, contain only lowercase letters, digits, hyphens and underscores, start with a lowercase letter, and end with a lowercase letter or a digit.
        :param pulumi.Input[str] location: The location is a GCP region. Currently only `us-central1` is supported.
        :param pulumi.Input[bool] logging_enabled: Whether stack driver logging is enabled for the instance.
        :param pulumi.Input[str] name: Instance resource name formatted as: `projects/[PROJECT_ID]/instances/[INSTANCE_ID]`. Name should not be populated when creating an instance since it is provided in the `instance_id` field.
        :param pulumi.Input[str] parent: Resource name of the project containing the instance. Format: `projects/[PROJECT_ID]`.
        :param pulumi.Input[str] state: State of the instance.
        """
        pulumi.set(__self__, "project", project)
        if feature_policy is not None:
            pulumi.set(__self__, "feature_policy", feature_policy)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if logging_enabled is not None:
            pulumi.set(__self__, "logging_enabled", logging_enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent is not None:
            pulumi.set(__self__, "parent", parent)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="featurePolicy")
    def feature_policy(self) -> Optional[pulumi.Input['GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyArgs']]:
        """
        The policy to define whether or not RBE features can be used or how they can be used.
        """
        return pulumi.get(self, "feature_policy")

    @feature_policy.setter
    def feature_policy(self, value: Optional[pulumi.Input['GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyArgs']]):
        pulumi.set(self, "feature_policy", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the created instance. A valid `instance_id` must: be 6-50 characters long, contain only lowercase letters, digits, hyphens and underscores, start with a lowercase letter, and end with a lowercase letter or a digit.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location is a GCP region. Currently only `us-central1` is supported.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="loggingEnabled")
    def logging_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether stack driver logging is enabled for the instance.
        """
        return pulumi.get(self, "logging_enabled")

    @logging_enabled.setter
    def logging_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "logging_enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Instance resource name formatted as: `projects/[PROJECT_ID]/instances/[INSTANCE_ID]`. Name should not be populated when creating an instance since it is provided in the `instance_id` field.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        """
        Resource name of the project containing the instance. Format: `projects/[PROJECT_ID]`.
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        State of the instance.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 feature_policy: Optional[pulumi.Input[pulumi.InputType['GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyArgs']]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logging_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new instance in the specified region. Returns a long running operation which contains an instance on completion. While the long running operation is in progress, any call to `GetInstance` returns an instance in state `CREATING`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyArgs']] feature_policy: The policy to define whether or not RBE features can be used or how they can be used.
        :param pulumi.Input[str] instance_id: ID of the created instance. A valid `instance_id` must: be 6-50 characters long, contain only lowercase letters, digits, hyphens and underscores, start with a lowercase letter, and end with a lowercase letter or a digit.
        :param pulumi.Input[str] location: The location is a GCP region. Currently only `us-central1` is supported.
        :param pulumi.Input[bool] logging_enabled: Whether stack driver logging is enabled for the instance.
        :param pulumi.Input[str] name: Instance resource name formatted as: `projects/[PROJECT_ID]/instances/[INSTANCE_ID]`. Name should not be populated when creating an instance since it is provided in the `instance_id` field.
        :param pulumi.Input[str] parent: Resource name of the project containing the instance. Format: `projects/[PROJECT_ID]`.
        :param pulumi.Input[str] state: State of the instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new instance in the specified region. Returns a long running operation which contains an instance on completion. While the long running operation is in progress, any call to `GetInstance` returns an instance in state `CREATING`.

        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 feature_policy: Optional[pulumi.Input[pulumi.InputType['GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyArgs']]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logging_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
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
            __props__ = InstanceArgs.__new__(InstanceArgs)

            __props__.__dict__["feature_policy"] = feature_policy
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["location"] = location
            __props__.__dict__["logging_enabled"] = logging_enabled
            __props__.__dict__["name"] = name
            __props__.__dict__["parent"] = parent
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["state"] = state
        super(Instance, __self__).__init__(
            'google-native:remotebuildexecution/v1alpha:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InstanceArgs.__new__(InstanceArgs)

        __props__.__dict__["feature_policy"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["logging_enabled"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["state"] = None
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="featurePolicy")
    def feature_policy(self) -> pulumi.Output['outputs.GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyResponse']:
        """
        The policy to define whether or not RBE features can be used or how they can be used.
        """
        return pulumi.get(self, "feature_policy")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location is a GCP region. Currently only `us-central1` is supported.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="loggingEnabled")
    def logging_enabled(self) -> pulumi.Output[bool]:
        """
        Whether stack driver logging is enabled for the instance.
        """
        return pulumi.get(self, "logging_enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Instance resource name formatted as: `projects/[PROJECT_ID]/instances/[INSTANCE_ID]`. Name should not be populated when creating an instance since it is provided in the `instance_id` field.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the instance.
        """
        return pulumi.get(self, "state")

