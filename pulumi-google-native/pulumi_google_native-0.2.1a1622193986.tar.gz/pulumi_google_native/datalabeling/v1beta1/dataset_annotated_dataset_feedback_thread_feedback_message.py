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

__all__ = ['DatasetAnnotatedDatasetFeedbackThreadFeedbackMessageArgs', 'DatasetAnnotatedDatasetFeedbackThreadFeedbackMessage']

@pulumi.input_type
class DatasetAnnotatedDatasetFeedbackThreadFeedbackMessageArgs:
    def __init__(__self__, *,
                 annotated_dataset_id: pulumi.Input[str],
                 dataset_id: pulumi.Input[str],
                 feedback_thread_id: pulumi.Input[str],
                 project: pulumi.Input[str],
                 body: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operator_feedback_metadata: Optional[pulumi.Input['GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataArgs']] = None,
                 requester_feedback_metadata: Optional[pulumi.Input['GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataArgs']] = None):
        """
        The set of arguments for constructing a DatasetAnnotatedDatasetFeedbackThreadFeedbackMessage resource.
        :param pulumi.Input[str] body: String content of the feedback. Maximum of 10000 characters.
        :param pulumi.Input[str] create_time: Create time.
        :param pulumi.Input[str] image: The image storing this feedback if the feedback is an image representing operator's comments.
        :param pulumi.Input[str] name: Name of the feedback message in a feedback thread. Format: 'project/{project_id}/datasets/{dataset_id}/annotatedDatasets/{annotated_dataset_id}/feedbackThreads/{feedback_thread_id}/feedbackMessage/{feedback_message_id}'
        """
        pulumi.set(__self__, "annotated_dataset_id", annotated_dataset_id)
        pulumi.set(__self__, "dataset_id", dataset_id)
        pulumi.set(__self__, "feedback_thread_id", feedback_thread_id)
        pulumi.set(__self__, "project", project)
        if body is not None:
            pulumi.set(__self__, "body", body)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if image is not None:
            pulumi.set(__self__, "image", image)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if operator_feedback_metadata is not None:
            pulumi.set(__self__, "operator_feedback_metadata", operator_feedback_metadata)
        if requester_feedback_metadata is not None:
            pulumi.set(__self__, "requester_feedback_metadata", requester_feedback_metadata)

    @property
    @pulumi.getter(name="annotatedDatasetId")
    def annotated_dataset_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "annotated_dataset_id")

    @annotated_dataset_id.setter
    def annotated_dataset_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "annotated_dataset_id", value)

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "dataset_id")

    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "dataset_id", value)

    @property
    @pulumi.getter(name="feedbackThreadId")
    def feedback_thread_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "feedback_thread_id")

    @feedback_thread_id.setter
    def feedback_thread_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "feedback_thread_id", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        """
        String content of the feedback. Maximum of 10000 characters.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Create time.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[str]]:
        """
        The image storing this feedback if the feedback is an image representing operator's comments.
        """
        return pulumi.get(self, "image")

    @image.setter
    def image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the feedback message in a feedback thread. Format: 'project/{project_id}/datasets/{dataset_id}/annotatedDatasets/{annotated_dataset_id}/feedbackThreads/{feedback_thread_id}/feedbackMessage/{feedback_message_id}'
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="operatorFeedbackMetadata")
    def operator_feedback_metadata(self) -> Optional[pulumi.Input['GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataArgs']]:
        return pulumi.get(self, "operator_feedback_metadata")

    @operator_feedback_metadata.setter
    def operator_feedback_metadata(self, value: Optional[pulumi.Input['GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataArgs']]):
        pulumi.set(self, "operator_feedback_metadata", value)

    @property
    @pulumi.getter(name="requesterFeedbackMetadata")
    def requester_feedback_metadata(self) -> Optional[pulumi.Input['GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataArgs']]:
        return pulumi.get(self, "requester_feedback_metadata")

    @requester_feedback_metadata.setter
    def requester_feedback_metadata(self, value: Optional[pulumi.Input['GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataArgs']]):
        pulumi.set(self, "requester_feedback_metadata", value)


class DatasetAnnotatedDatasetFeedbackThreadFeedbackMessage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotated_dataset_id: Optional[pulumi.Input[str]] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 dataset_id: Optional[pulumi.Input[str]] = None,
                 feedback_thread_id: Optional[pulumi.Input[str]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operator_feedback_metadata: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 requester_feedback_metadata: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataArgs']]] = None,
                 __props__=None):
        """
        Create a FeedbackMessage object.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: String content of the feedback. Maximum of 10000 characters.
        :param pulumi.Input[str] create_time: Create time.
        :param pulumi.Input[str] image: The image storing this feedback if the feedback is an image representing operator's comments.
        :param pulumi.Input[str] name: Name of the feedback message in a feedback thread. Format: 'project/{project_id}/datasets/{dataset_id}/annotatedDatasets/{annotated_dataset_id}/feedbackThreads/{feedback_thread_id}/feedbackMessage/{feedback_message_id}'
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatasetAnnotatedDatasetFeedbackThreadFeedbackMessageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a FeedbackMessage object.

        :param str resource_name: The name of the resource.
        :param DatasetAnnotatedDatasetFeedbackThreadFeedbackMessageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatasetAnnotatedDatasetFeedbackThreadFeedbackMessageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotated_dataset_id: Optional[pulumi.Input[str]] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 dataset_id: Optional[pulumi.Input[str]] = None,
                 feedback_thread_id: Optional[pulumi.Input[str]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operator_feedback_metadata: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 requester_feedback_metadata: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataArgs']]] = None,
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
            __props__ = DatasetAnnotatedDatasetFeedbackThreadFeedbackMessageArgs.__new__(DatasetAnnotatedDatasetFeedbackThreadFeedbackMessageArgs)

            if annotated_dataset_id is None and not opts.urn:
                raise TypeError("Missing required property 'annotated_dataset_id'")
            __props__.__dict__["annotated_dataset_id"] = annotated_dataset_id
            __props__.__dict__["body"] = body
            __props__.__dict__["create_time"] = create_time
            if dataset_id is None and not opts.urn:
                raise TypeError("Missing required property 'dataset_id'")
            __props__.__dict__["dataset_id"] = dataset_id
            if feedback_thread_id is None and not opts.urn:
                raise TypeError("Missing required property 'feedback_thread_id'")
            __props__.__dict__["feedback_thread_id"] = feedback_thread_id
            __props__.__dict__["image"] = image
            __props__.__dict__["name"] = name
            __props__.__dict__["operator_feedback_metadata"] = operator_feedback_metadata
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["requester_feedback_metadata"] = requester_feedback_metadata
        super(DatasetAnnotatedDatasetFeedbackThreadFeedbackMessage, __self__).__init__(
            'google-native:datalabeling/v1beta1:DatasetAnnotatedDatasetFeedbackThreadFeedbackMessage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DatasetAnnotatedDatasetFeedbackThreadFeedbackMessage':
        """
        Get an existing DatasetAnnotatedDatasetFeedbackThreadFeedbackMessage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatasetAnnotatedDatasetFeedbackThreadFeedbackMessageArgs.__new__(DatasetAnnotatedDatasetFeedbackThreadFeedbackMessageArgs)

        __props__.__dict__["body"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["image"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["operator_feedback_metadata"] = None
        __props__.__dict__["requester_feedback_metadata"] = None
        return DatasetAnnotatedDatasetFeedbackThreadFeedbackMessage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[str]:
        """
        String content of the feedback. Maximum of 10000 characters.
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Create time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def image(self) -> pulumi.Output[str]:
        """
        The image storing this feedback if the feedback is an image representing operator's comments.
        """
        return pulumi.get(self, "image")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the feedback message in a feedback thread. Format: 'project/{project_id}/datasets/{dataset_id}/annotatedDatasets/{annotated_dataset_id}/feedbackThreads/{feedback_thread_id}/feedbackMessage/{feedback_message_id}'
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operatorFeedbackMetadata")
    def operator_feedback_metadata(self) -> pulumi.Output['outputs.GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataResponse']:
        return pulumi.get(self, "operator_feedback_metadata")

    @property
    @pulumi.getter(name="requesterFeedbackMetadata")
    def requester_feedback_metadata(self) -> pulumi.Output['outputs.GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataResponse']:
        return pulumi.get(self, "requester_feedback_metadata")

