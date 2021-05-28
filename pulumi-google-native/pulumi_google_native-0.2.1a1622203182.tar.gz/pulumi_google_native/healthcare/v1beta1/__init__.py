# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .dataset import *
from .dataset_annotation_store import *
from .dataset_annotation_store_annotation import *
from .dataset_annotation_store_iam_policy import *
from .dataset_consent_store import *
from .dataset_consent_store_attribute_definition import *
from .dataset_consent_store_consent import *
from .dataset_consent_store_consent_artifact import *
from .dataset_consent_store_iam_policy import *
from .dataset_consent_store_user_data_mapping import *
from .dataset_dicom_store import *
from .dataset_dicom_store_iam_policy import *
from .dataset_fhir_store import *
from .dataset_fhir_store_iam_policy import *
from .dataset_hl7_v2_store import *
from .dataset_hl7_v2_store_iam_policy import *
from .dataset_hl7_v2_store_message import *
from .dataset_iam_policy import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from ... import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "google-native:healthcare/v1beta1:Dataset":
                return Dataset(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetAnnotationStore":
                return DatasetAnnotationStore(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetAnnotationStoreAnnotation":
                return DatasetAnnotationStoreAnnotation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetAnnotationStoreIamPolicy":
                return DatasetAnnotationStoreIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetConsentStore":
                return DatasetConsentStore(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetConsentStoreAttributeDefinition":
                return DatasetConsentStoreAttributeDefinition(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetConsentStoreConsent":
                return DatasetConsentStoreConsent(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetConsentStoreConsentArtifact":
                return DatasetConsentStoreConsentArtifact(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetConsentStoreIamPolicy":
                return DatasetConsentStoreIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetConsentStoreUserDataMapping":
                return DatasetConsentStoreUserDataMapping(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetDicomStore":
                return DatasetDicomStore(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetDicomStoreIamPolicy":
                return DatasetDicomStoreIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetFhirStore":
                return DatasetFhirStore(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetFhirStoreIamPolicy":
                return DatasetFhirStoreIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetHl7V2Store":
                return DatasetHl7V2Store(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetHl7V2StoreIamPolicy":
                return DatasetHl7V2StoreIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetHl7V2StoreMessage":
                return DatasetHl7V2StoreMessage(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:healthcare/v1beta1:DatasetIamPolicy":
                return DatasetIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("google-native", "healthcare/v1beta1", _module_instance)

_register_module()
