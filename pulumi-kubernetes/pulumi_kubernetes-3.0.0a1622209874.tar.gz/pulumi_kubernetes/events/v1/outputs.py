# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ... import core as _core
from ... import meta as _meta

__all__ = [
    'Event',
    'EventSeries',
]

@pulumi.output_type
class Event(dict):
    """
    Event is a report of an event somewhere in the cluster. It generally denotes some state change in the system. Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "eventTime":
            suggest = "event_time"
        elif key == "apiVersion":
            suggest = "api_version"
        elif key == "deprecatedCount":
            suggest = "deprecated_count"
        elif key == "deprecatedFirstTimestamp":
            suggest = "deprecated_first_timestamp"
        elif key == "deprecatedLastTimestamp":
            suggest = "deprecated_last_timestamp"
        elif key == "deprecatedSource":
            suggest = "deprecated_source"
        elif key == "reportingController":
            suggest = "reporting_controller"
        elif key == "reportingInstance":
            suggest = "reporting_instance"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in Event. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        Event.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        Event.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 event_time: str,
                 action: Optional[str] = None,
                 api_version: Optional[str] = None,
                 deprecated_count: Optional[int] = None,
                 deprecated_first_timestamp: Optional[str] = None,
                 deprecated_last_timestamp: Optional[str] = None,
                 deprecated_source: Optional['_core.v1.outputs.EventSource'] = None,
                 kind: Optional[str] = None,
                 metadata: Optional['_meta.v1.outputs.ObjectMeta'] = None,
                 note: Optional[str] = None,
                 reason: Optional[str] = None,
                 regarding: Optional['_core.v1.outputs.ObjectReference'] = None,
                 related: Optional['_core.v1.outputs.ObjectReference'] = None,
                 reporting_controller: Optional[str] = None,
                 reporting_instance: Optional[str] = None,
                 series: Optional['outputs.EventSeries'] = None,
                 type: Optional[str] = None):
        """
        Event is a report of an event somewhere in the cluster. It generally denotes some state change in the system. Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data.
        :param str event_time: eventTime is the time when this Event was first observed. It is required.
        :param str action: action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters.
        :param str api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param int deprecated_count: deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type.
        :param str deprecated_first_timestamp: deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
        :param str deprecated_last_timestamp: deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
        :param '_core.v1.EventSourceArgs' deprecated_source: deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type.
        :param str kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param '_meta.v1.ObjectMetaArgs' metadata: Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param str note: note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.
        :param str reason: reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters.
        :param '_core.v1.ObjectReferenceArgs' regarding: regarding contains the object this Event is about. In most cases it's an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.
        :param '_core.v1.ObjectReferenceArgs' related: related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.
        :param str reporting_controller: reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events.
        :param str reporting_instance: reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters.
        :param 'EventSeriesArgs' series: series is data about the Event series this event represents or nil if it's a singleton Event.
        :param str type: type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events.
        """
        pulumi.set(__self__, "event_time", event_time)
        if action is not None:
            pulumi.set(__self__, "action", action)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'events.k8s.io/v1')
        if deprecated_count is not None:
            pulumi.set(__self__, "deprecated_count", deprecated_count)
        if deprecated_first_timestamp is not None:
            pulumi.set(__self__, "deprecated_first_timestamp", deprecated_first_timestamp)
        if deprecated_last_timestamp is not None:
            pulumi.set(__self__, "deprecated_last_timestamp", deprecated_last_timestamp)
        if deprecated_source is not None:
            pulumi.set(__self__, "deprecated_source", deprecated_source)
        if kind is not None:
            pulumi.set(__self__, "kind", 'Event')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if note is not None:
            pulumi.set(__self__, "note", note)
        if reason is not None:
            pulumi.set(__self__, "reason", reason)
        if regarding is not None:
            pulumi.set(__self__, "regarding", regarding)
        if related is not None:
            pulumi.set(__self__, "related", related)
        if reporting_controller is not None:
            pulumi.set(__self__, "reporting_controller", reporting_controller)
        if reporting_instance is not None:
            pulumi.set(__self__, "reporting_instance", reporting_instance)
        if series is not None:
            pulumi.set(__self__, "series", series)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="eventTime")
    def event_time(self) -> str:
        """
        eventTime is the time when this Event was first observed. It is required.
        """
        return pulumi.get(self, "event_time")

    @property
    @pulumi.getter
    def action(self) -> Optional[str]:
        """
        action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter(name="deprecatedCount")
    def deprecated_count(self) -> Optional[int]:
        """
        deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type.
        """
        return pulumi.get(self, "deprecated_count")

    @property
    @pulumi.getter(name="deprecatedFirstTimestamp")
    def deprecated_first_timestamp(self) -> Optional[str]:
        """
        deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
        """
        return pulumi.get(self, "deprecated_first_timestamp")

    @property
    @pulumi.getter(name="deprecatedLastTimestamp")
    def deprecated_last_timestamp(self) -> Optional[str]:
        """
        deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
        """
        return pulumi.get(self, "deprecated_last_timestamp")

    @property
    @pulumi.getter(name="deprecatedSource")
    def deprecated_source(self) -> Optional['_core.v1.outputs.EventSource']:
        """
        deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type.
        """
        return pulumi.get(self, "deprecated_source")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> Optional['_meta.v1.outputs.ObjectMeta']:
        """
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def note(self) -> Optional[str]:
        """
        note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.
        """
        return pulumi.get(self, "note")

    @property
    @pulumi.getter
    def reason(self) -> Optional[str]:
        """
        reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters.
        """
        return pulumi.get(self, "reason")

    @property
    @pulumi.getter
    def regarding(self) -> Optional['_core.v1.outputs.ObjectReference']:
        """
        regarding contains the object this Event is about. In most cases it's an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.
        """
        return pulumi.get(self, "regarding")

    @property
    @pulumi.getter
    def related(self) -> Optional['_core.v1.outputs.ObjectReference']:
        """
        related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.
        """
        return pulumi.get(self, "related")

    @property
    @pulumi.getter(name="reportingController")
    def reporting_controller(self) -> Optional[str]:
        """
        reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events.
        """
        return pulumi.get(self, "reporting_controller")

    @property
    @pulumi.getter(name="reportingInstance")
    def reporting_instance(self) -> Optional[str]:
        """
        reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters.
        """
        return pulumi.get(self, "reporting_instance")

    @property
    @pulumi.getter
    def series(self) -> Optional['outputs.EventSeries']:
        """
        series is data about the Event series this event represents or nil if it's a singleton Event.
        """
        return pulumi.get(self, "series")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class EventSeries(dict):
    """
    EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. How often to update the EventSeries is up to the event reporters. The default event reporter in "k8s.io/client-go/tools/events/event_broadcaster.go" shows how this struct is updated on heartbeats and can guide customized reporter implementations.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "lastObservedTime":
            suggest = "last_observed_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EventSeries. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EventSeries.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EventSeries.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 count: int,
                 last_observed_time: str):
        """
        EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. How often to update the EventSeries is up to the event reporters. The default event reporter in "k8s.io/client-go/tools/events/event_broadcaster.go" shows how this struct is updated on heartbeats and can guide customized reporter implementations.
        :param int count: count is the number of occurrences in this series up to the last heartbeat time.
        :param str last_observed_time: lastObservedTime is the time when last Event from the series was seen before last heartbeat.
        """
        pulumi.set(__self__, "count", count)
        pulumi.set(__self__, "last_observed_time", last_observed_time)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        count is the number of occurrences in this series up to the last heartbeat time.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="lastObservedTime")
    def last_observed_time(self) -> str:
        """
        lastObservedTime is the time when last Event from the series was seen before last heartbeat.
        """
        return pulumi.get(self, "last_observed_time")


