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

__all__ = ['ObjectIamPolicyArgs', 'ObjectIamPolicy']

@pulumi.input_type
class ObjectIamPolicyArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 object: pulumi.Input[str],
                 bindings: Optional[pulumi.Input[Sequence[pulumi.Input['ObjectIamPolicyBindingsItemArgs']]]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 generation: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 provisional_user_project: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 user_project: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ObjectIamPolicy resource.
        :param pulumi.Input[Sequence[pulumi.Input['ObjectIamPolicyBindingsItemArgs']]] bindings: An association between a role, which comes with a set of permissions, and members who may assume that role.
        :param pulumi.Input[str] etag: HTTP 1.1  Entity tag for the policy.
        :param pulumi.Input[str] kind: The kind of item this is. For policies, this is always storage#policy. This field is ignored on input.
        :param pulumi.Input[str] resource_id: The ID of the resource to which this policy belongs. Will be of the form projects/_/buckets/bucket for buckets, and projects/_/buckets/bucket/objects/object for objects. A specific generation may be specified by appending #generationNumber to the end of the object name, e.g. projects/_/buckets/my-bucket/objects/data.txt#17. The current generation can be denoted with #0. This field is ignored on input.
        :param pulumi.Input[int] version: The IAM policy format version.
        """
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "object", object)
        if bindings is not None:
            pulumi.set(__self__, "bindings", bindings)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if generation is not None:
            pulumi.set(__self__, "generation", generation)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if provisional_user_project is not None:
            pulumi.set(__self__, "provisional_user_project", provisional_user_project)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if user_project is not None:
            pulumi.set(__self__, "user_project", user_project)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def object(self) -> pulumi.Input[str]:
        return pulumi.get(self, "object")

    @object.setter
    def object(self, value: pulumi.Input[str]):
        pulumi.set(self, "object", value)

    @property
    @pulumi.getter
    def bindings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ObjectIamPolicyBindingsItemArgs']]]]:
        """
        An association between a role, which comes with a set of permissions, and members who may assume that role.
        """
        return pulumi.get(self, "bindings")

    @bindings.setter
    def bindings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ObjectIamPolicyBindingsItemArgs']]]]):
        pulumi.set(self, "bindings", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        HTTP 1.1  Entity tag for the policy.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "generation")

    @generation.setter
    def generation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "generation", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        The kind of item this is. For policies, this is always storage#policy. This field is ignored on input.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="provisionalUserProject")
    def provisional_user_project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "provisional_user_project")

    @provisional_user_project.setter
    def provisional_user_project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisional_user_project", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the resource to which this policy belongs. Will be of the form projects/_/buckets/bucket for buckets, and projects/_/buckets/bucket/objects/object for objects. A specific generation may be specified by appending #generationNumber to the end of the object name, e.g. projects/_/buckets/my-bucket/objects/data.txt#17. The current generation can be denoted with #0. This field is ignored on input.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="userProject")
    def user_project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "user_project")

    @user_project.setter
    def user_project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_project", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        """
        The IAM policy format version.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class ObjectIamPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bindings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObjectIamPolicyBindingsItemArgs']]]]] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 generation: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 object: Optional[pulumi.Input[str]] = None,
                 provisional_user_project: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 user_project: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Updates an IAM policy for the specified object.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObjectIamPolicyBindingsItemArgs']]]] bindings: An association between a role, which comes with a set of permissions, and members who may assume that role.
        :param pulumi.Input[str] etag: HTTP 1.1  Entity tag for the policy.
        :param pulumi.Input[str] kind: The kind of item this is. For policies, this is always storage#policy. This field is ignored on input.
        :param pulumi.Input[str] resource_id: The ID of the resource to which this policy belongs. Will be of the form projects/_/buckets/bucket for buckets, and projects/_/buckets/bucket/objects/object for objects. A specific generation may be specified by appending #generationNumber to the end of the object name, e.g. projects/_/buckets/my-bucket/objects/data.txt#17. The current generation can be denoted with #0. This field is ignored on input.
        :param pulumi.Input[int] version: The IAM policy format version.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ObjectIamPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Updates an IAM policy for the specified object.

        :param str resource_name: The name of the resource.
        :param ObjectIamPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ObjectIamPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bindings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObjectIamPolicyBindingsItemArgs']]]]] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 generation: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 object: Optional[pulumi.Input[str]] = None,
                 provisional_user_project: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 user_project: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None,
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
            __props__ = ObjectIamPolicyArgs.__new__(ObjectIamPolicyArgs)

            __props__.__dict__["bindings"] = bindings
            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["etag"] = etag
            __props__.__dict__["generation"] = generation
            __props__.__dict__["kind"] = kind
            if object is None and not opts.urn:
                raise TypeError("Missing required property 'object'")
            __props__.__dict__["object"] = object
            __props__.__dict__["provisional_user_project"] = provisional_user_project
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["user_project"] = user_project
            __props__.__dict__["version"] = version
        super(ObjectIamPolicy, __self__).__init__(
            'google-native:storage/v1:ObjectIamPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ObjectIamPolicy':
        """
        Get an existing ObjectIamPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ObjectIamPolicyArgs.__new__(ObjectIamPolicyArgs)

        __props__.__dict__["bindings"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["version"] = None
        return ObjectIamPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bindings(self) -> pulumi.Output[Sequence['outputs.ObjectIamPolicyBindingsItemResponse']]:
        """
        An association between a role, which comes with a set of permissions, and members who may assume that role.
        """
        return pulumi.get(self, "bindings")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        HTTP 1.1  Entity tag for the policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of item this is. For policies, this is always storage#policy. This field is ignored on input.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        The ID of the resource to which this policy belongs. Will be of the form projects/_/buckets/bucket for buckets, and projects/_/buckets/bucket/objects/object for objects. A specific generation may be specified by appending #generationNumber to the end of the object name, e.g. projects/_/buckets/my-bucket/objects/data.txt#17. The current generation can be denoted with #0. This field is ignored on input.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        The IAM policy format version.
        """
        return pulumi.get(self, "version")

