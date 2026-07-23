# -*- coding: utf-8 -*-
from construct import Struct, Int64ul, Int32ul, Int32sl, RepeatUntil, Byte, Int16ul

from etl.dtyp import Sid
from etl.parsers.kernel.core import declare, Mof
from etl.utils import WString, CString
from etl.wmi import EventTraceGroup


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_PROCESS, version=3, event_types=[1, 2, 3, 4, 39])
class Process_V3_TypeGroup1(Mof):
    pattern = Struct(
        "UniqueProcessKey" / Int64ul,       # Pointer
        "ProcessId" / Int32ul,
        "ParentId" / Int32ul,
        "SessionId" / Int32ul,
        "ExitStatus" / Int32sl,
        "DirectoryTableBase" / Int64ul,     # Pointer
        "Sid" / Sid,
        "ImageFileName" / CString,
        "CommandLine" / WString
    )

    def get_image_file_name(self) -> str:
        pass

    def get_command_line(self) -> str:
        pass

    def get_package_full_name(self) -> str:
        pass

    def get_application_id(self) -> str:
        pass

    def get_exit_status(self) -> int:
        pass

    def get_process_id(self) -> int:
        pass

    def get_parent_id(self) -> int:
        pass


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_PROCESS, version=4, event_types=[1, 2, 3, 4, 39])
class Process_V4_TypeGroup1(Mof):
    pattern = Struct(
        "UniqueProcessKey" / Int64ul,       # Pointer
        "ProcessId" / Int32ul,
        "ParentId" / Int32ul,
        "SessionId" / Int32ul,
        "ExitStatus" / Int32sl,
        "DirectoryTableBase" / Int64ul,     # Pointer
        "Flags" / Int32ul,
        "UserSID_blob" / Byte[16],
        "Sid" / Sid,
        "ImageFileName" / CString,
        "CommandLine" / WString,
        "PackageFullName" / WString,
        "ApplicationId" / WString
    )

    def get_image_file_name(self) -> str:
        pass

    def get_command_line(self) -> str:
        pass

    def get_package_full_name(self) -> str:
        pass

    def get_application_id(self) -> str:
        pass

    def get_exit_status(self) -> int:
        pass

    def get_process_id(self) -> int:
        pass

    def get_parent_id(self) -> int:
        pass


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_PROCESS, version=5, event_types=[39])
class Process_Defunct_TypeGroup1(Process_V4_TypeGroup1):
    pattern = Struct(
        *Process_V4_TypeGroup1.pattern.subcons,
        "ExitTime" / Int64ul
    )


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_PROCESS, version=3, event_types=[10])
class ImageLoad(Mof):
    pattern = Struct(
        "ImageBase" / Int64ul,
        "ImageSize" / Int64ul,
        "ProcessId" / Int32ul,
        "ImageChecksum" / Int32ul,
        "TimeDateStamp" / Int32ul,
        "SignatureLevel" / Byte,
        "SignatureType" / Byte,
        "Reserved0" / Int16ul,
        "DefaultBase" / Int64ul,
        "Reserved1" / Int32ul,
        "Reserved2" / Int32ul,
        "Reserved3" / Int32ul,
        "Reserved4" / Int32ul,
        "FileName" / WString
    )

    def get_image_filename(self) -> str:
        pass

    def get_process_id(self) -> int:
        pass

    def get_image_base(self) -> int:
        pass

    def get_image_size(self) -> int:
        pass


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_PROCESS, version=2, event_types=[11])
class Process_Terminate_TypeGroup1(Mof):
    pattern = Struct(
        "ProcessId" / Int32ul
    )

    def get_process_id(self):
        pass
