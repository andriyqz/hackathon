from abc import ABC, abstractmethod
from typing import Any
from sqlalchemy import Column


class BaseFilter(ABC):
    def __init__(self, field_name: str, value: Any):
        self.field_name = field_name
        self.value = value

    @abstractmethod
    def apply(self, model, query):
        pass


class EqualsFilter(BaseFilter):
    def apply(self, model, query):
        column = getattr(model, self.field_name)
        return query.filter(column == self.value)
    

class GreaterThanFilter(BaseFilter):
    def apply(self, model, query):
        column = getattr(model, self.field_name)
        return query.filter(column > self.value)
    
class LessThanFilter(BaseFilter):
    def apply(self, model, query):
        column = getattr(model, self.field_name)
        return query.filter(column < self.value)


def apply_filters(query_params: dict, mapping: dict):
    """
    query_params: (Request.query_params)
    mapping: dict, where key - parameter name, value - filter class
    """
    filters = []
    for key, value in query_params.items():
        if value is not None and key in mapping:
            filter_class = mapping[key]["class"]
            model = mapping[key]["field"]
            filters.append(filter_class(model, value))
    return filters