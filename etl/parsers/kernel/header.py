# -*- coding: utf-8 -*-
from construct import Struct, Int32ul, Int64ul
from datetime import datetime, timedelta, timezone

from etl.parsers.kernel.core import declare, Mof
from etl.utils import TimeZoneInformation, WString
from etl.wmi import EventTraceGroup


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_HEADER, version=2, event_types=[0])
class EventTraceHeader(Mof):
    pattern = Struct(
        "BufferSize" / Int32ul,
        "Version" / Int32ul,
        "ProviderVersion" / Int32ul,
        "NumberOfProcessors" / Int32ul,
        "EndTime" / Int64ul,
        "TimerResolution" / Int32ul,
        "MaxFileSize" / Int32ul,
        "LogFileMode" / Int32ul,
        "BuffersWritten" / Int32ul,
        "StartBuffers" / Int32ul,
        "PointerSize" / Int32ul,
        "EventsLost" / Int32ul,
        "CPUSpeed" / Int32ul,
        "LoggerName" / Int64ul,
        "LogFileName" / Int64ul,
        "TimeZoneInformation" / TimeZoneInformation,
        "BootTime" / Int64ul,
        "PerfFreq" / Int64ul,
        "StartTime" / Int64ul,
        "ReservedFlags" / Int32ul,
        "BuffersLost" / Int32ul,
        "SessionNameString" / WString,
        "LogFileNameString" / WString
    )

    def get_session_name(self) -> str:
        pass

    def get_log_filename(self) -> str:
        pass

    def get_boot_time(self) -> datetime:
        pass

    def get_start_time(self) -> datetime:
        pass

    def get_end_time(self) -> datetime:
        pass

@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_HEADER, version=2, event_types=[5, 32])
class Header_Extension_TypeGroup(Mof):
    pattern = Struct(
        "GroupMask1" / Int32ul,
        "GroupMask2" / Int32ul,
        "GroupMask3" / Int32ul,
        "GroupMask4" / Int32ul,
        "GroupMask5" / Int32ul,
        "GroupMask6" / Int32ul,
        "GroupMask7" / Int32ul,
        "GroupMask8" / Int32ul,
        "KernelEventVersion" / Int32ul
    )


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_HEADER, version=0, event_types=[0])
class EventTrace_V0_Header(Mof):
    pattern = Struct(
        "BufferSize" / Int32ul,
        "Version" / Int32ul,
        "ProviderVersion" / Int32ul,
        "NumberOfProcessors" / Int32ul,
        "EndTime" / Int64ul,
        "TimerResolution" / Int32ul,
        "MaxFileSize" / Int32ul,
        "LogFileMode" / Int32ul,
        "BuffersWritten" / Int32ul,
        "StartBuffers" / Int32ul,
        "PointerSize" / Int32ul,
        "EventsLost" / Int32ul,
        "CPUSpeed" / Int32ul,
        "LoggerName" / Int32ul,
        "LogFileName" / Int32ul,
        "TimeZoneInformation" / TimeZoneInformation,
        "BootTime" / Int64ul,
        "PerfFreq" / Int64ul,
        "StartTime" / Int64ul,
        "ReservedFlags" / Int32ul,
        "BuffersLost" / Int32ul,
        "SessionNameString" / WString,
        "LogFileNameString" / WString
    )

