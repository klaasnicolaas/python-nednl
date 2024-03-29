"""Asynchronous Python client for National Energy Dashboard NL."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, TypeVar

from mashumaro import field_options
from mashumaro.config import BaseConfig
from mashumaro.mixins.dict import DataClassDictMixin
from mashumaro.mixins.orjson import DataClassORJSONMixin

_ResultDataT = TypeVar("_ResultDataT")


@dataclass
class NedDataMixin(DataClassDictMixin):
    """Mixin for dataclasses with a 'data' attribute."""

    # pylint: disable-next=too-few-public-methods
    class Config(BaseConfig):
        """Configuration for mashumaro."""

        serialize_by_alias = True


@dataclass
class BaseResponse(Generic[_ResultDataT], NedDataMixin, DataClassORJSONMixin):
    """Base object representing the API response."""

    data: _ResultDataT = field(metadata=field_options(alias="hydra:member"))
    items: int = field(metadata=field_options(alias="hydra:totalItems"))


@dataclass(slots=True)
class Activity(NedDataMixin, DataClassORJSONMixin):
    """Object representing an activity from National Energy Dashboard NL."""

    id: int  # noqa: A003, RUF100
    name: str


@dataclass(slots=True)
class Granularity(NedDataMixin, DataClassORJSONMixin):
    """Object representing an granularity from National Energy Dashboard NL."""

    id: int  # noqa: A003, RUF100
    name: str


@dataclass(slots=True)
class Point(NedDataMixin, DataClassORJSONMixin):
    """Object representing an area from National Energy Dashboard NL."""

    id: int  # noqa: A003, RUF100
    name: str
    shortname: str = field(metadata=field_options(alias="nameshort"))


@dataclass(slots=True)
class Type(NedDataMixin, DataClassORJSONMixin):
    """Object representing an type from National Energy Dashboard NL."""

    id: int  # noqa: A003, RUF100
    name: str
    shortname: str = field(metadata=field_options(alias="nameshort"))


@dataclass(slots=True)
class ActivitiesResponse(BaseResponse[list[Activity]]):
    """Object representing an Activities API response."""


@dataclass(slots=True)
class GranularitiesResponse(BaseResponse[list[Granularity]]):
    """Object representing an Granularities API response."""


@dataclass(slots=True)
class PointsResponse(BaseResponse[list[Point]]):
    """Object representing an Points API response."""


@dataclass(slots=True)
class TypesResponse(BaseResponse[list[Type]]):
    """Object representing an Types API response."""
