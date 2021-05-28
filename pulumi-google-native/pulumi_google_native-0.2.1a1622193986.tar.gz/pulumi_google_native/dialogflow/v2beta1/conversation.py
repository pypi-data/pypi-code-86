# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['ConversationArgs', 'Conversation']

@pulumi.input_type
class ConversationArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 project: pulumi.Input[str],
                 conversation_id: Optional[pulumi.Input[str]] = None,
                 conversation_profile: Optional[pulumi.Input[str]] = None,
                 conversation_stage: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Conversation resource.
        :param pulumi.Input[str] conversation_profile: Required. The Conversation Profile to be used to configure this Conversation. This field cannot be updated. Format: `projects//locations//conversationProfiles/`.
        :param pulumi.Input[str] conversation_stage: The stage of a conversation. It indicates whether the virtual agent or a human agent is handling the conversation. If the conversation is created with the conversation profile that has Dialogflow config set, defaults to ConversationStage.VIRTUAL_AGENT_STAGE; Otherwise, defaults to ConversationStage.HUMAN_ASSIST_STAGE. If the conversation is created with the conversation profile that has Dialogflow config set but explicitly sets conversation_stage to ConversationStage.HUMAN_ASSIST_STAGE, it skips ConversationStage.VIRTUAL_AGENT_STAGE stage and directly goes to ConversationStage.HUMAN_ASSIST_STAGE.
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "project", project)
        if conversation_id is not None:
            pulumi.set(__self__, "conversation_id", conversation_id)
        if conversation_profile is not None:
            pulumi.set(__self__, "conversation_profile", conversation_profile)
        if conversation_stage is not None:
            pulumi.set(__self__, "conversation_stage", conversation_stage)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="conversationId")
    def conversation_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "conversation_id")

    @conversation_id.setter
    def conversation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "conversation_id", value)

    @property
    @pulumi.getter(name="conversationProfile")
    def conversation_profile(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The Conversation Profile to be used to configure this Conversation. This field cannot be updated. Format: `projects//locations//conversationProfiles/`.
        """
        return pulumi.get(self, "conversation_profile")

    @conversation_profile.setter
    def conversation_profile(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "conversation_profile", value)

    @property
    @pulumi.getter(name="conversationStage")
    def conversation_stage(self) -> Optional[pulumi.Input[str]]:
        """
        The stage of a conversation. It indicates whether the virtual agent or a human agent is handling the conversation. If the conversation is created with the conversation profile that has Dialogflow config set, defaults to ConversationStage.VIRTUAL_AGENT_STAGE; Otherwise, defaults to ConversationStage.HUMAN_ASSIST_STAGE. If the conversation is created with the conversation profile that has Dialogflow config set but explicitly sets conversation_stage to ConversationStage.HUMAN_ASSIST_STAGE, it skips ConversationStage.VIRTUAL_AGENT_STAGE stage and directly goes to ConversationStage.HUMAN_ASSIST_STAGE.
        """
        return pulumi.get(self, "conversation_stage")

    @conversation_stage.setter
    def conversation_stage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "conversation_stage", value)


class Conversation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 conversation_id: Optional[pulumi.Input[str]] = None,
                 conversation_profile: Optional[pulumi.Input[str]] = None,
                 conversation_stage: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new conversation. Conversations are auto-completed after 24 hours. Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage. For Automated Agent Stage, there will be a dialogflow agent responding to user queries. For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation. If Conversation.conversation_profile is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an Intent with Intent.live_agent_handoff is triggered, conversation will transfer to Assist Stage.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] conversation_profile: Required. The Conversation Profile to be used to configure this Conversation. This field cannot be updated. Format: `projects//locations//conversationProfiles/`.
        :param pulumi.Input[str] conversation_stage: The stage of a conversation. It indicates whether the virtual agent or a human agent is handling the conversation. If the conversation is created with the conversation profile that has Dialogflow config set, defaults to ConversationStage.VIRTUAL_AGENT_STAGE; Otherwise, defaults to ConversationStage.HUMAN_ASSIST_STAGE. If the conversation is created with the conversation profile that has Dialogflow config set but explicitly sets conversation_stage to ConversationStage.HUMAN_ASSIST_STAGE, it skips ConversationStage.VIRTUAL_AGENT_STAGE stage and directly goes to ConversationStage.HUMAN_ASSIST_STAGE.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConversationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new conversation. Conversations are auto-completed after 24 hours. Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage. For Automated Agent Stage, there will be a dialogflow agent responding to user queries. For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation. If Conversation.conversation_profile is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an Intent with Intent.live_agent_handoff is triggered, conversation will transfer to Assist Stage.

        :param str resource_name: The name of the resource.
        :param ConversationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConversationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 conversation_id: Optional[pulumi.Input[str]] = None,
                 conversation_profile: Optional[pulumi.Input[str]] = None,
                 conversation_stage: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
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
            __props__ = ConversationArgs.__new__(ConversationArgs)

            __props__.__dict__["conversation_id"] = conversation_id
            __props__.__dict__["conversation_profile"] = conversation_profile
            __props__.__dict__["conversation_stage"] = conversation_stage
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["end_time"] = None
            __props__.__dict__["lifecycle_state"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["phone_number"] = None
            __props__.__dict__["start_time"] = None
        super(Conversation, __self__).__init__(
            'google-native:dialogflow/v2beta1:Conversation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Conversation':
        """
        Get an existing Conversation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConversationArgs.__new__(ConversationArgs)

        __props__.__dict__["conversation_profile"] = None
        __props__.__dict__["conversation_stage"] = None
        __props__.__dict__["end_time"] = None
        __props__.__dict__["lifecycle_state"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["phone_number"] = None
        __props__.__dict__["start_time"] = None
        return Conversation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="conversationProfile")
    def conversation_profile(self) -> pulumi.Output[str]:
        """
        Required. The Conversation Profile to be used to configure this Conversation. This field cannot be updated. Format: `projects//locations//conversationProfiles/`.
        """
        return pulumi.get(self, "conversation_profile")

    @property
    @pulumi.getter(name="conversationStage")
    def conversation_stage(self) -> pulumi.Output[str]:
        """
        The stage of a conversation. It indicates whether the virtual agent or a human agent is handling the conversation. If the conversation is created with the conversation profile that has Dialogflow config set, defaults to ConversationStage.VIRTUAL_AGENT_STAGE; Otherwise, defaults to ConversationStage.HUMAN_ASSIST_STAGE. If the conversation is created with the conversation profile that has Dialogflow config set but explicitly sets conversation_stage to ConversationStage.HUMAN_ASSIST_STAGE, it skips ConversationStage.VIRTUAL_AGENT_STAGE stage and directly goes to ConversationStage.HUMAN_ASSIST_STAGE.
        """
        return pulumi.get(self, "conversation_stage")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[str]:
        """
        The time the conversation was finished.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> pulumi.Output[str]:
        """
        The current state of the Conversation.
        """
        return pulumi.get(self, "lifecycle_state")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The unique identifier of this conversation. Format: `projects//locations//conversations/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Output['outputs.GoogleCloudDialogflowV2beta1ConversationPhoneNumberResponse']:
        """
        Required if the conversation is to be connected over telephony.
        """
        return pulumi.get(self, "phone_number")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        The time the conversation was started.
        """
        return pulumi.get(self, "start_time")

