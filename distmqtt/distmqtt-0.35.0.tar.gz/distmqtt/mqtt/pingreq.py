# Copyright (c) 2015 Nicolas JOUANIN
#
# See the file license.txt for copying permission.
from distmqtt.mqtt.packet import MQTTPacket, MQTTFixedHeader, PINGREQ
from distmqtt.errors import DistMQTTException


class PingReqPacket(MQTTPacket):
    VARIABLE_HEADER = None
    PAYLOAD = None

    def __init__(self, fixed: MQTTFixedHeader = None):
        if fixed is None:
            header = MQTTFixedHeader(PINGREQ, 0x00)
        else:
            if fixed.packet_type != PINGREQ:
                raise DistMQTTException(
                    "Invalid fixed packet type %s for PingReqPacket init" % fixed.packet_type
                )
            header = fixed
        super().__init__(header)
        self.variable_header = None
        self.payload = None
