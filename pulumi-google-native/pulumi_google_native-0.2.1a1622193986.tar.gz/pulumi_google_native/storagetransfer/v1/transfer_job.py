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

__all__ = ['TransferJobArgs', 'TransferJob']

@pulumi.input_type
class TransferJobArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 latest_operation_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_config: Optional[pulumi.Input['NotificationConfigArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input['ScheduleArgs']] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 transfer_spec: Optional[pulumi.Input['TransferSpecArgs']] = None):
        """
        The set of arguments for constructing a TransferJob resource.
        :param pulumi.Input[str] description: A description provided by the user for the job. Its max length is 1024 bytes when Unicode-encoded.
        :param pulumi.Input[str] latest_operation_name: The name of the most recently started TransferOperation of this JobConfig. Present if and only if at least one TransferOperation has been created for this JobConfig.
        :param pulumi.Input[str] name: A unique name (within the transfer project) assigned when the job is created. If this field is empty in a CreateTransferJobRequest, Storage Transfer Service will assign a unique name. Otherwise, the specified name is used as the unique name for this job. If the specified name is in use by a job, the creation request fails with an ALREADY_EXISTS error. This name must start with `"transferJobs/"` prefix and end with a letter or a number, and should be no more than 128 characters. This name must not start with 'transferJobs/OPI'. 'transferJobs/OPI' is a reserved prefix. Example: `"transferJobs/^(?!OPI)[A-Za-z0-9-._~]*[A-Za-z0-9]$"` Invalid job names will fail with an INVALID_ARGUMENT error.
        :param pulumi.Input['NotificationConfigArgs'] notification_config: Notification configuration.
        :param pulumi.Input[str] project: The ID of the Google Cloud Platform Project that owns the job.
        :param pulumi.Input['ScheduleArgs'] schedule: Specifies schedule for the transfer job. This is an optional field. When the field is not set, the job will never execute a transfer, unless you invoke RunTransferJob or update the job to have a non-empty schedule.
        :param pulumi.Input[str] status: Status of the job. This value MUST be specified for `CreateTransferJobRequests`. **Note:** The effect of the new job status takes place during a subsequent job run. For example, if you change the job status from ENABLED to DISABLED, and an operation spawned by the transfer is running, the status change would not affect the current operation.
        :param pulumi.Input['TransferSpecArgs'] transfer_spec: Transfer specification.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if latest_operation_name is not None:
            pulumi.set(__self__, "latest_operation_name", latest_operation_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_config is not None:
            pulumi.set(__self__, "notification_config", notification_config)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if transfer_spec is not None:
            pulumi.set(__self__, "transfer_spec", transfer_spec)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description provided by the user for the job. Its max length is 1024 bytes when Unicode-encoded.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="latestOperationName")
    def latest_operation_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the most recently started TransferOperation of this JobConfig. Present if and only if at least one TransferOperation has been created for this JobConfig.
        """
        return pulumi.get(self, "latest_operation_name")

    @latest_operation_name.setter
    def latest_operation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "latest_operation_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique name (within the transfer project) assigned when the job is created. If this field is empty in a CreateTransferJobRequest, Storage Transfer Service will assign a unique name. Otherwise, the specified name is used as the unique name for this job. If the specified name is in use by a job, the creation request fails with an ALREADY_EXISTS error. This name must start with `"transferJobs/"` prefix and end with a letter or a number, and should be no more than 128 characters. This name must not start with 'transferJobs/OPI'. 'transferJobs/OPI' is a reserved prefix. Example: `"transferJobs/^(?!OPI)[A-Za-z0-9-._~]*[A-Za-z0-9]$"` Invalid job names will fail with an INVALID_ARGUMENT error.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> Optional[pulumi.Input['NotificationConfigArgs']]:
        """
        Notification configuration.
        """
        return pulumi.get(self, "notification_config")

    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input['NotificationConfigArgs']]):
        pulumi.set(self, "notification_config", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Google Cloud Platform Project that owns the job.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input['ScheduleArgs']]:
        """
        Specifies schedule for the transfer job. This is an optional field. When the field is not set, the job will never execute a transfer, unless you invoke RunTransferJob or update the job to have a non-empty schedule.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input['ScheduleArgs']]):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the job. This value MUST be specified for `CreateTransferJobRequests`. **Note:** The effect of the new job status takes place during a subsequent job run. For example, if you change the job status from ENABLED to DISABLED, and an operation spawned by the transfer is running, the status change would not affect the current operation.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="transferSpec")
    def transfer_spec(self) -> Optional[pulumi.Input['TransferSpecArgs']]:
        """
        Transfer specification.
        """
        return pulumi.get(self, "transfer_spec")

    @transfer_spec.setter
    def transfer_spec(self, value: Optional[pulumi.Input['TransferSpecArgs']]):
        pulumi.set(self, "transfer_spec", value)


class TransferJob(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 latest_operation_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_config: Optional[pulumi.Input[pulumi.InputType['NotificationConfigArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ScheduleArgs']]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 transfer_spec: Optional[pulumi.Input[pulumi.InputType['TransferSpecArgs']]] = None,
                 __props__=None):
        """
        Creates a transfer job that runs periodically.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description provided by the user for the job. Its max length is 1024 bytes when Unicode-encoded.
        :param pulumi.Input[str] latest_operation_name: The name of the most recently started TransferOperation of this JobConfig. Present if and only if at least one TransferOperation has been created for this JobConfig.
        :param pulumi.Input[str] name: A unique name (within the transfer project) assigned when the job is created. If this field is empty in a CreateTransferJobRequest, Storage Transfer Service will assign a unique name. Otherwise, the specified name is used as the unique name for this job. If the specified name is in use by a job, the creation request fails with an ALREADY_EXISTS error. This name must start with `"transferJobs/"` prefix and end with a letter or a number, and should be no more than 128 characters. This name must not start with 'transferJobs/OPI'. 'transferJobs/OPI' is a reserved prefix. Example: `"transferJobs/^(?!OPI)[A-Za-z0-9-._~]*[A-Za-z0-9]$"` Invalid job names will fail with an INVALID_ARGUMENT error.
        :param pulumi.Input[pulumi.InputType['NotificationConfigArgs']] notification_config: Notification configuration.
        :param pulumi.Input[str] project: The ID of the Google Cloud Platform Project that owns the job.
        :param pulumi.Input[pulumi.InputType['ScheduleArgs']] schedule: Specifies schedule for the transfer job. This is an optional field. When the field is not set, the job will never execute a transfer, unless you invoke RunTransferJob or update the job to have a non-empty schedule.
        :param pulumi.Input[str] status: Status of the job. This value MUST be specified for `CreateTransferJobRequests`. **Note:** The effect of the new job status takes place during a subsequent job run. For example, if you change the job status from ENABLED to DISABLED, and an operation spawned by the transfer is running, the status change would not affect the current operation.
        :param pulumi.Input[pulumi.InputType['TransferSpecArgs']] transfer_spec: Transfer specification.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TransferJobArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a transfer job that runs periodically.

        :param str resource_name: The name of the resource.
        :param TransferJobArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TransferJobArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 latest_operation_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_config: Optional[pulumi.Input[pulumi.InputType['NotificationConfigArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ScheduleArgs']]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 transfer_spec: Optional[pulumi.Input[pulumi.InputType['TransferSpecArgs']]] = None,
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
            __props__ = TransferJobArgs.__new__(TransferJobArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["latest_operation_name"] = latest_operation_name
            __props__.__dict__["name"] = name
            __props__.__dict__["notification_config"] = notification_config
            __props__.__dict__["project"] = project
            __props__.__dict__["schedule"] = schedule
            __props__.__dict__["status"] = status
            __props__.__dict__["transfer_spec"] = transfer_spec
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["deletion_time"] = None
            __props__.__dict__["last_modification_time"] = None
        super(TransferJob, __self__).__init__(
            'google-native:storagetransfer/v1:TransferJob',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TransferJob':
        """
        Get an existing TransferJob resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TransferJobArgs.__new__(TransferJobArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["deletion_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["last_modification_time"] = None
        __props__.__dict__["latest_operation_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notification_config"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["schedule"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["transfer_spec"] = None
        return TransferJob(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The time that the transfer job was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="deletionTime")
    def deletion_time(self) -> pulumi.Output[str]:
        """
        The time that the transfer job was deleted.
        """
        return pulumi.get(self, "deletion_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        A description provided by the user for the job. Its max length is 1024 bytes when Unicode-encoded.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastModificationTime")
    def last_modification_time(self) -> pulumi.Output[str]:
        """
        The time that the transfer job was last modified.
        """
        return pulumi.get(self, "last_modification_time")

    @property
    @pulumi.getter(name="latestOperationName")
    def latest_operation_name(self) -> pulumi.Output[str]:
        """
        The name of the most recently started TransferOperation of this JobConfig. Present if and only if at least one TransferOperation has been created for this JobConfig.
        """
        return pulumi.get(self, "latest_operation_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique name (within the transfer project) assigned when the job is created. If this field is empty in a CreateTransferJobRequest, Storage Transfer Service will assign a unique name. Otherwise, the specified name is used as the unique name for this job. If the specified name is in use by a job, the creation request fails with an ALREADY_EXISTS error. This name must start with `"transferJobs/"` prefix and end with a letter or a number, and should be no more than 128 characters. This name must not start with 'transferJobs/OPI'. 'transferJobs/OPI' is a reserved prefix. Example: `"transferJobs/^(?!OPI)[A-Za-z0-9-._~]*[A-Za-z0-9]$"` Invalid job names will fail with an INVALID_ARGUMENT error.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> pulumi.Output['outputs.NotificationConfigResponse']:
        """
        Notification configuration.
        """
        return pulumi.get(self, "notification_config")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the Google Cloud Platform Project that owns the job.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output['outputs.ScheduleResponse']:
        """
        Specifies schedule for the transfer job. This is an optional field. When the field is not set, the job will never execute a transfer, unless you invoke RunTransferJob or update the job to have a non-empty schedule.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the job. This value MUST be specified for `CreateTransferJobRequests`. **Note:** The effect of the new job status takes place during a subsequent job run. For example, if you change the job status from ENABLED to DISABLED, and an operation spawned by the transfer is running, the status change would not affect the current operation.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="transferSpec")
    def transfer_spec(self) -> pulumi.Output['outputs.TransferSpecResponse']:
        """
        Transfer specification.
        """
        return pulumi.get(self, "transfer_spec")

