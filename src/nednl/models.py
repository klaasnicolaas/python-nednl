"""Asynchronous Python client for National Energy Dashboard NL."""

from __future__ import annotations

from dataclasses import dataclass, field

from mashumaro import field_options
from mashumaro.mixins.orjson import DataClassORJSONMixin


@dataclass
class PointsResponse(DataClassORJSONMixin):
    """Object representing an Points API response."""

    points: list[Point] = field(metadata=field_options(alias="hydra:member"))
    items: int = field(metadata=field_options(alias="hydra:totalItems"))


@dataclass
class Point(DataClassORJSONMixin):
    """Object representing an area from National Energy Dashboard NL."""

    point_id: int = field(metadata=field_options(alias="id"))
    name: str
    nameshort: str
