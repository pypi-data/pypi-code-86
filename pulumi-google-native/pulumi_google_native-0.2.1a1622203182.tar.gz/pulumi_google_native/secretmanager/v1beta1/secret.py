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

__all__ = ['SecretArgs', 'Secret']

@pulumi.input_type
class SecretArgs:
    def __init__(__self__, *,
                 project: pulumi.Input[str],
                 secret_id: pulumi.Input[str],
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 replication: Optional[pulumi.Input['ReplicationArgs']] = None):
        """
        The set of arguments for constructing a Secret resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels assigned to this Secret. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `\p{Ll}\p{Lo}{0,62}` Label values must be between 0 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}` No more than 64 labels can be assigned to a given resource.
        :param pulumi.Input['ReplicationArgs'] replication: Required. Immutable. The replication policy of the secret data attached to the Secret. The replication policy cannot be changed after the Secret has been created.
        """
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "secret_id", secret_id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if replication is not None:
            pulumi.set(__self__, "replication", replication)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "secret_id")

    @secret_id.setter
    def secret_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret_id", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The labels assigned to this Secret. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `\p{Ll}\p{Lo}{0,62}` Label values must be between 0 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}` No more than 64 labels can be assigned to a given resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def replication(self) -> Optional[pulumi.Input['ReplicationArgs']]:
        """
        Required. Immutable. The replication policy of the secret data attached to the Secret. The replication policy cannot be changed after the Secret has been created.
        """
        return pulumi.get(self, "replication")

    @replication.setter
    def replication(self, value: Optional[pulumi.Input['ReplicationArgs']]):
        pulumi.set(self, "replication", value)


class Secret(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 replication: Optional[pulumi.Input[pulumi.InputType['ReplicationArgs']]] = None,
                 secret_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new Secret containing no SecretVersions.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels assigned to this Secret. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `\p{Ll}\p{Lo}{0,62}` Label values must be between 0 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}` No more than 64 labels can be assigned to a given resource.
        :param pulumi.Input[pulumi.InputType['ReplicationArgs']] replication: Required. Immutable. The replication policy of the secret data attached to the Secret. The replication policy cannot be changed after the Secret has been created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecretArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Secret containing no SecretVersions.

        :param str resource_name: The name of the resource.
        :param SecretArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecretArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 replication: Optional[pulumi.Input[pulumi.InputType['ReplicationArgs']]] = None,
                 secret_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = SecretArgs.__new__(SecretArgs)

            __props__.__dict__["labels"] = labels
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["replication"] = replication
            if secret_id is None and not opts.urn:
                raise TypeError("Missing required property 'secret_id'")
            __props__.__dict__["secret_id"] = secret_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
        super(Secret, __self__).__init__(
            'google-native:secretmanager/v1beta1:Secret',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Secret':
        """
        Get an existing Secret resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecretArgs.__new__(SecretArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["replication"] = None
        return Secret(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time at which the Secret was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The labels assigned to this Secret. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `\p{Ll}\p{Lo}{0,62}` Label values must be between 0 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}` No more than 64 labels can be assigned to a given resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the Secret in the format `projects/*/secrets/*`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def replication(self) -> pulumi.Output['outputs.ReplicationResponse']:
        """
        Required. Immutable. The replication policy of the secret data attached to the Secret. The replication policy cannot be changed after the Secret has been created.
        """
        return pulumi.get(self, "replication")

