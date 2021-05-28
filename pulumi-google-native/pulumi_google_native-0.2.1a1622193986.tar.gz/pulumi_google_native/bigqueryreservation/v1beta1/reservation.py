# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ReservationArgs', 'Reservation']

@pulumi.input_type
class ReservationArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 project: pulumi.Input[str],
                 ignore_idle_slots: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 reservation_id: Optional[pulumi.Input[str]] = None,
                 slot_capacity: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Reservation resource.
        :param pulumi.Input[bool] ignore_idle_slots: If false, any query using this reservation will use idle slots from other reservations within the same admin project. If true, a query using this reservation will execute with the slot capacity specified above at most.
        :param pulumi.Input[str] name: The resource name of the reservation, e.g., `projects/*/locations/*/reservations/team1-prod`.
        :param pulumi.Input[str] slot_capacity: Minimum slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the unit of parallelism. Queries using this reservation might use more slots during runtime if ignore_idle_slots is set to false. If the new reservation's slot capacity exceed the parent's slot capacity or if total slot capacity of the new reservation and its siblings exceeds the parent's slot capacity, the request will fail with `google.rpc.Code.RESOURCE_EXHAUSTED`.
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "project", project)
        if ignore_idle_slots is not None:
            pulumi.set(__self__, "ignore_idle_slots", ignore_idle_slots)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if reservation_id is not None:
            pulumi.set(__self__, "reservation_id", reservation_id)
        if slot_capacity is not None:
            pulumi.set(__self__, "slot_capacity", slot_capacity)

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
    @pulumi.getter(name="ignoreIdleSlots")
    def ignore_idle_slots(self) -> Optional[pulumi.Input[bool]]:
        """
        If false, any query using this reservation will use idle slots from other reservations within the same admin project. If true, a query using this reservation will execute with the slot capacity specified above at most.
        """
        return pulumi.get(self, "ignore_idle_slots")

    @ignore_idle_slots.setter
    def ignore_idle_slots(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_idle_slots", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the reservation, e.g., `projects/*/locations/*/reservations/team1-prod`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="reservationId")
    def reservation_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "reservation_id")

    @reservation_id.setter
    def reservation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reservation_id", value)

    @property
    @pulumi.getter(name="slotCapacity")
    def slot_capacity(self) -> Optional[pulumi.Input[str]]:
        """
        Minimum slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the unit of parallelism. Queries using this reservation might use more slots during runtime if ignore_idle_slots is set to false. If the new reservation's slot capacity exceed the parent's slot capacity or if total slot capacity of the new reservation and its siblings exceeds the parent's slot capacity, the request will fail with `google.rpc.Code.RESOURCE_EXHAUSTED`.
        """
        return pulumi.get(self, "slot_capacity")

    @slot_capacity.setter
    def slot_capacity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slot_capacity", value)


class Reservation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ignore_idle_slots: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 reservation_id: Optional[pulumi.Input[str]] = None,
                 slot_capacity: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new reservation resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] ignore_idle_slots: If false, any query using this reservation will use idle slots from other reservations within the same admin project. If true, a query using this reservation will execute with the slot capacity specified above at most.
        :param pulumi.Input[str] name: The resource name of the reservation, e.g., `projects/*/locations/*/reservations/team1-prod`.
        :param pulumi.Input[str] slot_capacity: Minimum slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the unit of parallelism. Queries using this reservation might use more slots during runtime if ignore_idle_slots is set to false. If the new reservation's slot capacity exceed the parent's slot capacity or if total slot capacity of the new reservation and its siblings exceeds the parent's slot capacity, the request will fail with `google.rpc.Code.RESOURCE_EXHAUSTED`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReservationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new reservation resource.

        :param str resource_name: The name of the resource.
        :param ReservationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReservationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ignore_idle_slots: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 reservation_id: Optional[pulumi.Input[str]] = None,
                 slot_capacity: Optional[pulumi.Input[str]] = None,
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
            __props__ = ReservationArgs.__new__(ReservationArgs)

            __props__.__dict__["ignore_idle_slots"] = ignore_idle_slots
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["reservation_id"] = reservation_id
            __props__.__dict__["slot_capacity"] = slot_capacity
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["update_time"] = None
        super(Reservation, __self__).__init__(
            'google-native:bigqueryreservation/v1beta1:Reservation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Reservation':
        """
        Get an existing Reservation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReservationArgs.__new__(ReservationArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["ignore_idle_slots"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["slot_capacity"] = None
        __props__.__dict__["update_time"] = None
        return Reservation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        Creation time of the reservation.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="ignoreIdleSlots")
    def ignore_idle_slots(self) -> pulumi.Output[bool]:
        """
        If false, any query using this reservation will use idle slots from other reservations within the same admin project. If true, a query using this reservation will execute with the slot capacity specified above at most.
        """
        return pulumi.get(self, "ignore_idle_slots")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the reservation, e.g., `projects/*/locations/*/reservations/team1-prod`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="slotCapacity")
    def slot_capacity(self) -> pulumi.Output[str]:
        """
        Minimum slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the unit of parallelism. Queries using this reservation might use more slots during runtime if ignore_idle_slots is set to false. If the new reservation's slot capacity exceed the parent's slot capacity or if total slot capacity of the new reservation and its siblings exceeds the parent's slot capacity, the request will fail with `google.rpc.Code.RESOURCE_EXHAUSTED`.
        """
        return pulumi.get(self, "slot_capacity")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Last update time of the reservation.
        """
        return pulumi.get(self, "update_time")

