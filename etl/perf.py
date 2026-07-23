# -*- coding: utf-8 -*-

from datetime import datetime, timezone, timedelta

from construct import Struct, Enum, Int64ul, Bytes, Int8ul, Container

from etl.parsers.kernel.core import Mof, build_mof
from etl.wmi import WmiTracePacket, wmi_trace_marker

PerfInfoTraceMarker = Enum(
    Int8ul,
    PERFINFO_TRACE_MARKER_32=0x10,
    PERFINFO_TRACE_MARKER_64=0x11
)

PerfInfoTraceRecord = Struct(
    "marker" / wmi_trace_marker(PerfInfoTraceMarker),
    "header" / WmiTracePacket,
    "timestamp" / Int64ul,
    "mof_data" / Bytes(lambda this: this.header.size - 16)
)


class PerfInfo:
    def __init__(self, source: Container):
        self.source = source

    def get_timestamp(self, boot_time: int) -> str:
        pass

    def get_mof(self) -> Mof:
        pass

