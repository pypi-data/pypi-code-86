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

__all__ = ['ProviderNoteArgs', 'ProviderNote']

@pulumi.input_type
class ProviderNoteArgs:
    def __init__(__self__, *,
                 provider_id: pulumi.Input[str],
                 attestation_authority: Optional[pulumi.Input['AttestationAuthorityArgs']] = None,
                 base_image: Optional[pulumi.Input['BasisArgs']] = None,
                 build_type: Optional[pulumi.Input['BuildTypeArgs']] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 deployable: Optional[pulumi.Input['DeployableArgs']] = None,
                 discovery: Optional[pulumi.Input['DiscoveryArgs']] = None,
                 expiration_time: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 long_description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 note_id: Optional[pulumi.Input[str]] = None,
                 package: Optional[pulumi.Input['PackageArgs']] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 related_url: Optional[pulumi.Input[Sequence[pulumi.Input['RelatedUrlArgs']]]] = None,
                 short_description: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 upgrade: Optional[pulumi.Input['UpgradeNoteArgs']] = None,
                 vulnerability_type: Optional[pulumi.Input['VulnerabilityTypeArgs']] = None):
        """
        The set of arguments for constructing a ProviderNote resource.
        :param pulumi.Input['AttestationAuthorityArgs'] attestation_authority: A note describing an attestation role.
        :param pulumi.Input['BasisArgs'] base_image: A note describing a base image.
        :param pulumi.Input['BuildTypeArgs'] build_type: Build provenance type for a verifiable build.
        :param pulumi.Input[str] create_time: The time this note was created. This field can be used as a filter in list requests.
        :param pulumi.Input['DeployableArgs'] deployable: A note describing something that can be deployed.
        :param pulumi.Input['DiscoveryArgs'] discovery: A note describing a provider/analysis type.
        :param pulumi.Input[str] expiration_time: Time of expiration for this note, null if note does not expire.
        :param pulumi.Input[str] kind: This explicitly denotes which kind of note is specified. This field can be used as a filter in list requests.
        :param pulumi.Input[str] long_description: A detailed description of this `Note`.
        :param pulumi.Input[str] name: The name of the note in the form "projects/{provider_project_id}/notes/{NOTE_ID}"
        :param pulumi.Input['PackageArgs'] package: A note describing a package hosted by various package managers.
        :param pulumi.Input[Sequence[pulumi.Input['RelatedUrlArgs']]] related_url: URLs associated with this note
        :param pulumi.Input[str] short_description: A one sentence description of this `Note`.
        :param pulumi.Input[str] update_time: The time this note was last updated. This field can be used as a filter in list requests.
        :param pulumi.Input['UpgradeNoteArgs'] upgrade: A note describing an upgrade.
        :param pulumi.Input['VulnerabilityTypeArgs'] vulnerability_type: A package vulnerability type of note.
        """
        pulumi.set(__self__, "provider_id", provider_id)
        if attestation_authority is not None:
            pulumi.set(__self__, "attestation_authority", attestation_authority)
        if base_image is not None:
            pulumi.set(__self__, "base_image", base_image)
        if build_type is not None:
            pulumi.set(__self__, "build_type", build_type)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if deployable is not None:
            pulumi.set(__self__, "deployable", deployable)
        if discovery is not None:
            pulumi.set(__self__, "discovery", discovery)
        if expiration_time is not None:
            pulumi.set(__self__, "expiration_time", expiration_time)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if long_description is not None:
            pulumi.set(__self__, "long_description", long_description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if note_id is not None:
            pulumi.set(__self__, "note_id", note_id)
        if package is not None:
            pulumi.set(__self__, "package", package)
        if parent is not None:
            pulumi.set(__self__, "parent", parent)
        if related_url is not None:
            pulumi.set(__self__, "related_url", related_url)
        if short_description is not None:
            pulumi.set(__self__, "short_description", short_description)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)
        if upgrade is not None:
            pulumi.set(__self__, "upgrade", upgrade)
        if vulnerability_type is not None:
            pulumi.set(__self__, "vulnerability_type", vulnerability_type)

    @property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "provider_id")

    @provider_id.setter
    def provider_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider_id", value)

    @property
    @pulumi.getter(name="attestationAuthority")
    def attestation_authority(self) -> Optional[pulumi.Input['AttestationAuthorityArgs']]:
        """
        A note describing an attestation role.
        """
        return pulumi.get(self, "attestation_authority")

    @attestation_authority.setter
    def attestation_authority(self, value: Optional[pulumi.Input['AttestationAuthorityArgs']]):
        pulumi.set(self, "attestation_authority", value)

    @property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> Optional[pulumi.Input['BasisArgs']]:
        """
        A note describing a base image.
        """
        return pulumi.get(self, "base_image")

    @base_image.setter
    def base_image(self, value: Optional[pulumi.Input['BasisArgs']]):
        pulumi.set(self, "base_image", value)

    @property
    @pulumi.getter(name="buildType")
    def build_type(self) -> Optional[pulumi.Input['BuildTypeArgs']]:
        """
        Build provenance type for a verifiable build.
        """
        return pulumi.get(self, "build_type")

    @build_type.setter
    def build_type(self, value: Optional[pulumi.Input['BuildTypeArgs']]):
        pulumi.set(self, "build_type", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time this note was created. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def deployable(self) -> Optional[pulumi.Input['DeployableArgs']]:
        """
        A note describing something that can be deployed.
        """
        return pulumi.get(self, "deployable")

    @deployable.setter
    def deployable(self, value: Optional[pulumi.Input['DeployableArgs']]):
        pulumi.set(self, "deployable", value)

    @property
    @pulumi.getter
    def discovery(self) -> Optional[pulumi.Input['DiscoveryArgs']]:
        """
        A note describing a provider/analysis type.
        """
        return pulumi.get(self, "discovery")

    @discovery.setter
    def discovery(self, value: Optional[pulumi.Input['DiscoveryArgs']]):
        pulumi.set(self, "discovery", value)

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[pulumi.Input[str]]:
        """
        Time of expiration for this note, null if note does not expire.
        """
        return pulumi.get(self, "expiration_time")

    @expiration_time.setter
    def expiration_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_time", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        This explicitly denotes which kind of note is specified. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> Optional[pulumi.Input[str]]:
        """
        A detailed description of this `Note`.
        """
        return pulumi.get(self, "long_description")

    @long_description.setter
    def long_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "long_description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the note in the form "projects/{provider_project_id}/notes/{NOTE_ID}"
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="noteId")
    def note_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "note_id")

    @note_id.setter
    def note_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "note_id", value)

    @property
    @pulumi.getter
    def package(self) -> Optional[pulumi.Input['PackageArgs']]:
        """
        A note describing a package hosted by various package managers.
        """
        return pulumi.get(self, "package")

    @package.setter
    def package(self, value: Optional[pulumi.Input['PackageArgs']]):
        pulumi.set(self, "package", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter(name="relatedUrl")
    def related_url(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RelatedUrlArgs']]]]:
        """
        URLs associated with this note
        """
        return pulumi.get(self, "related_url")

    @related_url.setter
    def related_url(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RelatedUrlArgs']]]]):
        pulumi.set(self, "related_url", value)

    @property
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> Optional[pulumi.Input[str]]:
        """
        A one sentence description of this `Note`.
        """
        return pulumi.get(self, "short_description")

    @short_description.setter
    def short_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "short_description", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time this note was last updated. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)

    @property
    @pulumi.getter
    def upgrade(self) -> Optional[pulumi.Input['UpgradeNoteArgs']]:
        """
        A note describing an upgrade.
        """
        return pulumi.get(self, "upgrade")

    @upgrade.setter
    def upgrade(self, value: Optional[pulumi.Input['UpgradeNoteArgs']]):
        pulumi.set(self, "upgrade", value)

    @property
    @pulumi.getter(name="vulnerabilityType")
    def vulnerability_type(self) -> Optional[pulumi.Input['VulnerabilityTypeArgs']]:
        """
        A package vulnerability type of note.
        """
        return pulumi.get(self, "vulnerability_type")

    @vulnerability_type.setter
    def vulnerability_type(self, value: Optional[pulumi.Input['VulnerabilityTypeArgs']]):
        pulumi.set(self, "vulnerability_type", value)


class ProviderNote(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attestation_authority: Optional[pulumi.Input[pulumi.InputType['AttestationAuthorityArgs']]] = None,
                 base_image: Optional[pulumi.Input[pulumi.InputType['BasisArgs']]] = None,
                 build_type: Optional[pulumi.Input[pulumi.InputType['BuildTypeArgs']]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 deployable: Optional[pulumi.Input[pulumi.InputType['DeployableArgs']]] = None,
                 discovery: Optional[pulumi.Input[pulumi.InputType['DiscoveryArgs']]] = None,
                 expiration_time: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 long_description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 note_id: Optional[pulumi.Input[str]] = None,
                 package: Optional[pulumi.Input[pulumi.InputType['PackageArgs']]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 provider_id: Optional[pulumi.Input[str]] = None,
                 related_url: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RelatedUrlArgs']]]]] = None,
                 short_description: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 upgrade: Optional[pulumi.Input[pulumi.InputType['UpgradeNoteArgs']]] = None,
                 vulnerability_type: Optional[pulumi.Input[pulumi.InputType['VulnerabilityTypeArgs']]] = None,
                 __props__=None):
        """
        Creates a new `Note`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AttestationAuthorityArgs']] attestation_authority: A note describing an attestation role.
        :param pulumi.Input[pulumi.InputType['BasisArgs']] base_image: A note describing a base image.
        :param pulumi.Input[pulumi.InputType['BuildTypeArgs']] build_type: Build provenance type for a verifiable build.
        :param pulumi.Input[str] create_time: The time this note was created. This field can be used as a filter in list requests.
        :param pulumi.Input[pulumi.InputType['DeployableArgs']] deployable: A note describing something that can be deployed.
        :param pulumi.Input[pulumi.InputType['DiscoveryArgs']] discovery: A note describing a provider/analysis type.
        :param pulumi.Input[str] expiration_time: Time of expiration for this note, null if note does not expire.
        :param pulumi.Input[str] kind: This explicitly denotes which kind of note is specified. This field can be used as a filter in list requests.
        :param pulumi.Input[str] long_description: A detailed description of this `Note`.
        :param pulumi.Input[str] name: The name of the note in the form "projects/{provider_project_id}/notes/{NOTE_ID}"
        :param pulumi.Input[pulumi.InputType['PackageArgs']] package: A note describing a package hosted by various package managers.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RelatedUrlArgs']]]] related_url: URLs associated with this note
        :param pulumi.Input[str] short_description: A one sentence description of this `Note`.
        :param pulumi.Input[str] update_time: The time this note was last updated. This field can be used as a filter in list requests.
        :param pulumi.Input[pulumi.InputType['UpgradeNoteArgs']] upgrade: A note describing an upgrade.
        :param pulumi.Input[pulumi.InputType['VulnerabilityTypeArgs']] vulnerability_type: A package vulnerability type of note.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderNoteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new `Note`.

        :param str resource_name: The name of the resource.
        :param ProviderNoteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderNoteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attestation_authority: Optional[pulumi.Input[pulumi.InputType['AttestationAuthorityArgs']]] = None,
                 base_image: Optional[pulumi.Input[pulumi.InputType['BasisArgs']]] = None,
                 build_type: Optional[pulumi.Input[pulumi.InputType['BuildTypeArgs']]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 deployable: Optional[pulumi.Input[pulumi.InputType['DeployableArgs']]] = None,
                 discovery: Optional[pulumi.Input[pulumi.InputType['DiscoveryArgs']]] = None,
                 expiration_time: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 long_description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 note_id: Optional[pulumi.Input[str]] = None,
                 package: Optional[pulumi.Input[pulumi.InputType['PackageArgs']]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 provider_id: Optional[pulumi.Input[str]] = None,
                 related_url: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RelatedUrlArgs']]]]] = None,
                 short_description: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 upgrade: Optional[pulumi.Input[pulumi.InputType['UpgradeNoteArgs']]] = None,
                 vulnerability_type: Optional[pulumi.Input[pulumi.InputType['VulnerabilityTypeArgs']]] = None,
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
            __props__ = ProviderNoteArgs.__new__(ProviderNoteArgs)

            __props__.__dict__["attestation_authority"] = attestation_authority
            __props__.__dict__["base_image"] = base_image
            __props__.__dict__["build_type"] = build_type
            __props__.__dict__["create_time"] = create_time
            __props__.__dict__["deployable"] = deployable
            __props__.__dict__["discovery"] = discovery
            __props__.__dict__["expiration_time"] = expiration_time
            __props__.__dict__["kind"] = kind
            __props__.__dict__["long_description"] = long_description
            __props__.__dict__["name"] = name
            __props__.__dict__["note_id"] = note_id
            __props__.__dict__["package"] = package
            __props__.__dict__["parent"] = parent
            if provider_id is None and not opts.urn:
                raise TypeError("Missing required property 'provider_id'")
            __props__.__dict__["provider_id"] = provider_id
            __props__.__dict__["related_url"] = related_url
            __props__.__dict__["short_description"] = short_description
            __props__.__dict__["update_time"] = update_time
            __props__.__dict__["upgrade"] = upgrade
            __props__.__dict__["vulnerability_type"] = vulnerability_type
        super(ProviderNote, __self__).__init__(
            'google-native:containeranalysis/v1alpha1:ProviderNote',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ProviderNote':
        """
        Get an existing ProviderNote resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProviderNoteArgs.__new__(ProviderNoteArgs)

        __props__.__dict__["attestation_authority"] = None
        __props__.__dict__["base_image"] = None
        __props__.__dict__["build_type"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["deployable"] = None
        __props__.__dict__["discovery"] = None
        __props__.__dict__["expiration_time"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["long_description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["package"] = None
        __props__.__dict__["related_url"] = None
        __props__.__dict__["short_description"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["upgrade"] = None
        __props__.__dict__["vulnerability_type"] = None
        return ProviderNote(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attestationAuthority")
    def attestation_authority(self) -> pulumi.Output['outputs.AttestationAuthorityResponse']:
        """
        A note describing an attestation role.
        """
        return pulumi.get(self, "attestation_authority")

    @property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> pulumi.Output['outputs.BasisResponse']:
        """
        A note describing a base image.
        """
        return pulumi.get(self, "base_image")

    @property
    @pulumi.getter(name="buildType")
    def build_type(self) -> pulumi.Output['outputs.BuildTypeResponse']:
        """
        Build provenance type for a verifiable build.
        """
        return pulumi.get(self, "build_type")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time this note was created. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def deployable(self) -> pulumi.Output['outputs.DeployableResponse']:
        """
        A note describing something that can be deployed.
        """
        return pulumi.get(self, "deployable")

    @property
    @pulumi.getter
    def discovery(self) -> pulumi.Output['outputs.DiscoveryResponse']:
        """
        A note describing a provider/analysis type.
        """
        return pulumi.get(self, "discovery")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> pulumi.Output[str]:
        """
        Time of expiration for this note, null if note does not expire.
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        This explicitly denotes which kind of note is specified. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> pulumi.Output[str]:
        """
        A detailed description of this `Note`.
        """
        return pulumi.get(self, "long_description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the note in the form "projects/{provider_project_id}/notes/{NOTE_ID}"
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def package(self) -> pulumi.Output['outputs.PackageResponse']:
        """
        A note describing a package hosted by various package managers.
        """
        return pulumi.get(self, "package")

    @property
    @pulumi.getter(name="relatedUrl")
    def related_url(self) -> pulumi.Output[Sequence['outputs.RelatedUrlResponse']]:
        """
        URLs associated with this note
        """
        return pulumi.get(self, "related_url")

    @property
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> pulumi.Output[str]:
        """
        A one sentence description of this `Note`.
        """
        return pulumi.get(self, "short_description")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time this note was last updated. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def upgrade(self) -> pulumi.Output['outputs.UpgradeNoteResponse']:
        """
        A note describing an upgrade.
        """
        return pulumi.get(self, "upgrade")

    @property
    @pulumi.getter(name="vulnerabilityType")
    def vulnerability_type(self) -> pulumi.Output['outputs.VulnerabilityTypeResponse']:
        """
        A package vulnerability type of note.
        """
        return pulumi.get(self, "vulnerability_type")

