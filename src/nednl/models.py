"""Asynchronous Python client for National Energy Dashboard NL."""

from __future__ import annotations

from dataclasses import dataclass, field

from mashumaro import field_options
from mashumaro.mixins.orjson import DataClassORJSONMixin


@dataclass
class ActivitiesResponse(DataClassORJSONMixin):
    """Object representing an Activities API response."""

    data: list[Activity] = field(metadata=field_options(alias="hydra:member"))
    items: int = field(metadata=field_options(alias="hydra:totalItems"))


@dataclass
class GranularitiesResponse(DataClassORJSONMixin):
    """Object representing an Granularities API response."""

    data: list[Granularity] = field(metadata=field_options(alias="hydra:member"))
    items: int = field(metadata=field_options(alias="hydra:totalItems"))


@dataclass
class PointsResponse(DataClassORJSONMixin):
    """Object representing an Points API response."""

    data: list[Point] = field(metadata=field_options(alias="hydra:member"))
    items: int = field(metadata=field_options(alias="hydra:totalItems"))


@dataclass
class Activity(DataClassORJSONMixin):
    """Object representing an activity from National Energy Dashboard NL."""

    id: int  # noqa: A003, RUF100
    name: str


@dataclass
class Granularity(DataClassORJSONMixin):
    """Object representing an granularity from National Energy Dashboard NL."""

    id: int  # noqa: A003, RUF100
    name: str


@dataclass
class Point(DataClassORJSONMixin):
    """Object representing an area from National Energy Dashboard NL."""

    id: int  # noqa: A003, RUF100
    name: str
    nameshort: str
