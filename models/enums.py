import enum

class UserRole(enum.Enum):
    DELIVERY_POINT = "DELIVERY_POINT"
    LOGIST = "LOGIST"
    DRIVER = "DRIVER"


class RequestStatus(enum.Enum):
    NEW = "NEW"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    CANCELLED = "CANCELLED"


class TaskStatus(enum.Enum):
    ASSIGNED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class Priority(enum.Enum):
    NORMAL = "NORMAL"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"