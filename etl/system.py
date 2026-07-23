# -*- coding: utf-8 -*-

from construct import Struct, Computed, Int32ul, Int64ul, If, LazyBound, Bytes, Enum, Int8ul, Container

from etl.parsers.kernel.core import Mof, build_mof
from etl.wmi import wmi_trace_marker, WmiTracePacket

"""
Marker use by the parser to determiner if current trace is a system trace
"""
SystemTraceMarker = Enum(
    Int8ul,
    SYSTEM_TRACE_MARKER_32=0x01,
    SYSTEM_TRACE_MARKER_64=0x02,
    COMPACT_TRACE_MARKER_32=0x03,
    COMPACT_TRACE_MARKER_64=0x04,
)

SystemTraceHeader = Struct(
    "start_mark" / Computed(lambda this: this._io.tell()),
    "marker" / wmi_trace_marker(SystemTraceMarker),
    "header" / WmiTracePacket,
    "thread_id" / Int32ul,
    "process_id" / Int32ul,
    "system_time" / Int64ul,
    "kernel_time" / If(lambda this: this.marker.type.enum in [SystemTraceMarker.SYSTEM_TRACE_MARKER_32, SystemTraceMarker.SYSTEM_TRACE_MARKER_64], LazyBound(lambda: Int32ul)),
    "user_time" / If(lambda this: this.marker.type.enum in [SystemTraceMarker.SYSTEM_TRACE_MARKER_32, SystemTraceMarker.SYSTEM_TRACE_MARKER_64], LazyBound(lambda: Int32ul)),
    "sizeof" / Computed(lambda this: this._io.tell() - this.start_mark)
)


SystemTraceRecord = Struct(
    "system_header" / SystemTraceHeader,
    "mof_data" / Bytes(lambda this: this.system_header.header.size - this.system_header.sizeof)
)


class System:
    def __init__(self, source: Container):
        """
        :param source: SystemTrace
        """
        self.source = source

    def get_process_id(self) -> int:
        pass

    def get_thread_id(self) -> int:
        pass

    def get_mof(self) -> Mof:
        pass
