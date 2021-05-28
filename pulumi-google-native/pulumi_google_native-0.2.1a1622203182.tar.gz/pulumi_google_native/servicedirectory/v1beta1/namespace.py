# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['NamespaceArgs', 'Namespace']

@pulumi.input_type
class NamespaceArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 namespace_id: pulumi.Input[str],
                 project: pulumi.Input[str],
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Namespace resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Resource labels associated with this namespace. No more than 64 user labels can be associated with a given resource. Label keys and values can be no longer than 63 characters.
        :param pulumi.Input[str] name: Immutable. The resource name for the namespace in the format `projects/*/locations/*/namespaces/*`.
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "namespace_id", namespace_id)
        pulumi.set(__self__, "project", project)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "namespace_id")

    @namespace_id.setter
    def namespace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_id", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. Resource labels associated with this namespace. No more than 64 user labels can be associated with a given resource. Label keys and values can be no longer than 63 characters.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. The resource name for the namespace in the format `projects/*/locations/*/namespaces/*`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class Namespace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a namespace, and returns the new namespace.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Resource labels associated with this namespace. No more than 64 user labels can be associated with a given resource. Label keys and values can be no longer than 63 characters.
        :param pulumi.Input[str] name: Immutable. The resource name for the namespace in the format `projects/*/locations/*/namespaces/*`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a namespace, and returns the new namespace.

        :param str resource_name: The name of the resource.
        :param NamespaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
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
            __props__ = NamespaceArgs.__new__(NamespaceArgs)

            __props__.__dict__["labels"] = labels
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if namespace_id is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_id'")
            __props__.__dict__["namespace_id"] = namespace_id
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
        super(Namespace, __self__).__init__(
            'google-native:servicedirectory/v1beta1:Namespace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Namespace':
        """
        Get an existing Namespace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NamespaceArgs.__new__(NamespaceArgs)

        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        return Namespace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. Resource labels associated with this namespace. No more than 64 user labels can be associated with a given resource. Label keys and values can be no longer than 63 characters.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Immutable. The resource name for the namespace in the format `projects/*/locations/*/namespaces/*`.
        """
        return pulumi.get(self, "name")

