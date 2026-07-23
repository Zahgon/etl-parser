# -*- coding: utf-8 -*-
from etl.wmi import EventTraceGroup


class EtlException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidEtlFileHeader(EtlException):
    def __init__(self):
        super().__init__("Invalid ETL file header : first chunk is not a valid WmiLogType header")


class GroupNotFound(EtlException):
    def __init__(self, group: EventTraceGroup):
        super().__init__("No class handle this MOF group : %s"%group)


class VersionNotFound(EtlException):
    def __init__(self, group: EventTraceGroup, version: int):
        super().__init__("No class handle this group (%s) version : %s" % (group, version))


class EventTypeNotFound(EtlException):
    def __init__(self, group: EventTraceGroup, version: int, event_type: int):
        super().__init__("No class handle this group (%s) in version (%s) for event_type : %s" % (group, version, event_type))


class GuidNotFound(EtlException):
    def __init__(self, guid):
        super().__init__("No class handle this ETW provider : (%s)"%guid)


class EventIdNotFound(EtlException):
    def __init__(self, guid, event_id: int):
        super().__init__("No class handle this ETW provider (%s) for event id : (%s)"%(guid, event_id))


class EtwVersionNotFound(EtlException):
    def __init__(self, guid, event_id: int, version: int):
        super().__init__("No class handle this ETW provider (%s) for event id : (%s) for version : %s"%(guid, event_id, version))


class TlMetaDataNotFound(EtlException):
    def __init__(self):
        super().__init__("Meta data not found for trace logging parser")


class TlUnhandledTag(EtlException):
    def __init__(self, tag):
        super().__init__("Cannot read tag type %s"%tag)


class InvalidType(EtlException):
    def __init__(self, type):
        super().__init__("The type %s is invalid"%type)