from enum import Enum


class ValuedEnum(Enum):
    @classmethod
    def values(cls):
        return list(map(lambda c: c.value, cls))
        