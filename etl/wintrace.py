# -*- coding: utf-8 -*-
from construct import Struct, Int16ul, Const, Int32ul, AlignedStruct, Computed, Bytes, Container

from etl.parsers.etw.core import Etw, build_etw, Guid as EtwGuid
from etl.utils import Guid

WinTraceHeader = Struct(
    "size" / Int16ul,
    "marker" / Const(0x9000, Int16ul),
    "event_id" / Int16ul,
    "flags" / Int16ul,
    "provider_id" / Guid,
    "thread_id" / Int32ul,
    "process_id" / Int32ul
)

WinTraceRecord = AlignedStruct(8,
    "mark1" / Computed(lambda this: this._io.tell()),
    "event_header" / WinTraceHeader,
    "mark2" / Computed(lambda this: this._io.tell()),
    "user_data" / Bytes(lambda this: this.event_header.size - (this.mark2 - this.mark1))
                               )


class WinTrace:

    def __init__(self, source: Container):
        """
        :param source Container: The EventTraceRecord Container once it's parsed
        """
        self.source = source

    def get_process_id(self) -> int:
        pass

    def get_thread_id(self) -> int:
        pass

    def parse_etw(self) -> Etw:
        pass
