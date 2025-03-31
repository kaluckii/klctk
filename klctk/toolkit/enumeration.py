from enum import Enum
from typing import List, Dict, Any


class Enumeration:
    _ATTR_FILTER_PREFIX = "_"

    def __class_getitem__(cls, item):
        return cls._get_child_dict()[item]

    @classmethod
    def _get_child_dict(cls):
        return {k: v for k, v in cls.__dict__.items() if not k.startswith(cls._ATTR_FILTER_PREFIX)}

    @classmethod
    def get_all_values(cls) -> List:
        return list(cls._get_child_dict().values())
    
    @classmethod
    def values_to_dict(cls) -> Dict[Any, Any]:
        return cls._get_child_dict()

    @classmethod
    def to_enum(cls) -> type[Enum]:
        members_dict = cls._get_child_dict()
        return Enum(cls.__name__, members_dict)
