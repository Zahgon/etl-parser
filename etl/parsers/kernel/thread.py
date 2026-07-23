# -*- coding: utf-8 -*-
from construct import Struct, Int32ul, Int64ul, Byte

from etl.parsers.kernel.core import declare, Mof
from etl.wmi import EventTraceGroup


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_THREAD, version=2, event_types=[1, 2, 3, 4])
class Thread_V2_TypeGroup1(Mof):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ThreadId" / Int32ul,
        "StackBase" / Int64ul,
        "StackLimit" / Int64ul,
        "UserStackBase" / Int64ul,
        "UserStackLimit" / Int64ul,
        "StartAddr" / Int64ul,
        "Win32StartAddr" / Int64ul,
        "TebBase" / Int64ul,
        "SubProcessTag" / Int32ul
    )

    def get_process_id(self) -> int:
        pass

    def get_thread_id(self) -> int:
        pass

    def get_subprocess_tag(self) -> int:
        pass


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_THREAD, version=3, event_types=[1, 2, 3, 4])
class Thread_TypeGroup1(Mof):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ThreadId" / Int32ul,
        "StackBase" / Int64ul,
        "StackLimit" / Int64ul,
        "UserStackBase" / Int64ul,
        "UserStackLimit" / Int64ul,
        "Affinity" / Int64ul,
        "Win32StartAddr" / Int64ul,
        "TebBase" / Int64ul,
        "SubProcessTag" / Int32ul,
        "BasePriority" / Byte,
        "PagePriority" / Byte,
        "IoPriority" / Byte,
        "ThreadFlags" / Byte
    )

    def get_process_id(self) -> int:
        pass

    def get_thread_id(self) -> int:
        pass

    def get_subprocess_tag(self) -> int:
        pass

    def get_thread_flags(self) -> int:
        pass


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_THREAD, version=2, event_types=[37])
class CompCS(Mof):
    pattern = Struct()
