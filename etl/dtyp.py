# -*- coding: utf-8 -*-

from construct import Struct, Int8ul, Byte, Int32ul, Array, Const

Sid = Struct(
    "Revision" / Const(0x01, Int8ul),
    "SubAuthorityCount" / Int8ul,
    "IdentifierAuthority" / Byte[6],
    "SubAuthority" / Array(lambda this: this.SubAuthorityCount, Int32ul)
)