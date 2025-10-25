"""Asynchronous Python client for National Energy Dashboard NL."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from mashumaro import field_options
from mashumaro.config import BaseConfig
from mashumaro.mixins.dict import DataClassDictMixin
from mashumaro.mixins.orjson import DataClassORJSONMixin


@dataclass
class NedDataMixin(DataClassDictMixin):
    """Mixin for dataclasses with a 'data' attribute."""

    # pylint: disable-next=too-few-public-methods
    class Config(BaseConfig):
        """Configuration for mashumaro."""

        serialize_by_alias = True


@dataclass
class BaseResponse[ResultDataT](NedDataMixin, DataClassORJSONMixin):
    """Base object representing the API response."""

    data: ResultDataT = field(metadata=field_options(alias="hydra:member"))
    items: int = field(metadata=field_options(alias="hydra:totalItems"))


@dataclass(slots=True)
class Activity(NedDataMixin, DataClassORJSONMixin):
    """Object representing an activity from National Energy Dashboard NL."""

    id: int  # noqa: A003, RUF100
    name: str


@dataclass(slots=True)
class Classification(NedDataMixin, DataClassORJSONMixin):
    """Object representing an classification from National Energy Dashboard NL."""

    id: int  # noqa: A003, RUF100
    name: str


@dataclass(slots=True)
class Granularity(NedDataMixin, DataClassORJSONMixin):
    """Object representing an granularity from National Energy Dashboard NL."""

    id: int  # noqa: A003, RUF100
    name: str


@dataclass(slots=True)
class GranularityTimezone(NedDataMixin, DataClassORJSONMixin):
    """Object representing an granularity timezone from National Energy Dashboard NL."""

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
class Utilization(NedDataMixin, DataClassORJSONMixin):
    """Object representing an utilization from National Energy Dashboard NL."""

    id: int  # noqa: A003, RUF100
    capacity: int
    volume: int
    percentage: float
    emission: int
    emission_factor: float = field(metadata=field_options(alias="emissionfactor"))
    valid_from: datetime = field(metadata=field_options(alias="validfrom"))
    valid_to: datetime = field(metadata=field_options(alias="validto"))
    last_update: datetime = field(metadata=field_options(alias="lastupdate"))


@dataclass(slots=True)
class ActivitiesResponse(BaseResponse[list[Activity]]):
    """Object representing an Activities API response."""


@dataclass(slots=True)
class ClassificationsResponse(BaseResponse[list[Classification]]):
    """Object representing an Classifications API response."""


@dataclass(slots=True)
class GranularitiesResponse(BaseResponse[list[Granularity]]):
    """Object representing an Granularities API response."""


@dataclass(slots=True)
class GranularityTimezonesResponse(BaseResponse[list[GranularityTimezone]]):
    """Object representing an GranularityTimezones API response."""


@dataclass(slots=True)
class PointsResponse(BaseResponse[list[Point]]):
    """Object representing an Points API response."""


@dataclass(slots=True)
class TypesResponse(BaseResponse[list[Type]]):
    """Object representing an Types API response."""


@dataclass(slots=True)
class UtilizationsResponse(BaseResponse[list[Utilization]]):
    """Object representing an Utilizations API response."""
