# -*- coding: utf-8 -*-
from construct import Struct, Int32ul, Int64ul

from etl.parsers.kernel.core import declare, Mof
from etl.wmi import EventTraceGroup


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_IO, version=3, event_types=[10, 11, 55, 56])
class DiskIo_TypeGroup1(Mof):
    pattern = Struct(
        "DiskNumber" / Int32ul,
        "IrpFlags" / Int32ul,
        "TransferSize" / Int32ul,
        "Reserved" / Int32ul,
        "ByteOffset" / Int64ul,
        "FileObject" / Int64ul,
        "Irp" / Int64ul,
        "HighResponseTime" / Int64ul,
        "IssuingThreadId" / Int32ul
    )

    def get_disk_number(self) -> int:
        pass

    def get_issuing_thread_id(self) -> int:
        pass

    def get_transfer_size(self) -> int:
        pass


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_IO, version=3, event_types=[14, 57])
class DiskIo_TypeGroup3(Mof):
    pattern = Struct(
        "DiskNumber" / Int32ul,
        "IrpFlags" / Int32ul,
        "HighResResponseTime" / Int64ul,
        "Irp" / Int32ul,
        "IssuingThreadId" / Int32ul
    )

    def get_disk_number(self) -> int:
        pass

    def get_issuing_thread_id(self) -> int:
        pass
