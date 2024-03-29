"""Asynchronous Python client for National Energy Dashboard NL."""

from __future__ import annotations

import asyncio
import socket
from dataclasses import dataclass
from importlib import metadata
from typing import Any, Self

from aiohttp import ClientError, ClientResponseError, ClientSession
from aiohttp.hdrs import METH_GET
from yarl import URL

from .exceptions import NedNLAuthenticationError, NedNLConnectionError, NedNLError
from .models import (
    ActivitiesResponse,
    Activity,
    Classification,
    ClassificationsResponse,
    GranularitiesResponse,
    Granularity,
    GranularityTimezone,
    GranularityTimezonesResponse,
    Point,
    PointsResponse,
    Type,
    TypesResponse,
)

VERSION = metadata.version(__package__)


@dataclass
class NedNL:
    """Main class for handling data fetching from National Energy Dashboard NL."""

    api_key: str
    request_timeout: float = 10.0
    session: ClientSession | None = None

    _close_session: bool = False

    async def _request(
        self,
        uri: str,
        *,
        method: str = METH_GET,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Handle a request to the National Energy Dashboard NL API.

        Args:
        ----
            uri: Request URI, without '/api/', for example, 'status'.
            method: HTTP method to use.
            params: Extra options to improve or limit the response.

        Returns:
        -------
            The response data from the API.

        Raises:
        ------
            NedNLAuthenticationError: If no API key is provided.
            NedNLConnectionError: If an error occurs while connecting to the API.
            NedNLError: If an unexpected response is received from the API.

        """
        url = URL.build(scheme="https", host="api.ned.nl", path="/v1/").join(URL(uri))

        if self.api_key is None or self.api_key == "":
            msg = "No API key provided."
            raise NedNLAuthenticationError(msg)

        headers = {
            "Accept": "application/ld+json",
            "User-Agent": f"python-nednl/{VERSION}",
            "X-AUTH-TOKEN": self.api_key,
        }

        if self.session is None:
            self.session = ClientSession()
            self._close_session = True

        try:
            async with asyncio.timeout(self.request_timeout):
                response = await self.session.request(
                    method,
                    url,
                    params=params,
                    headers=headers,
                    ssl=True,
                )
                response.raise_for_status()
        except TimeoutError as exception:
            msg = "Timeout occurred while connecting to NED NL API."
            raise NedNLConnectionError(msg) from exception
        except ClientResponseError as exception:
            if exception.status == 403:
                msg = "Invalid or expired API key provided."
                raise NedNLAuthenticationError(msg) from exception
            msg = "Error occurred while communicating with NED NL API."
            raise NedNLConnectionError(msg) from exception
        except (ClientError, socket.gaierror) as exception:
            msg = "Error occurred while communicating with NED NL API."
            raise NedNLConnectionError(msg) from exception

        content_type = response.headers.get("Content-Type", "")
        text = await response.text()
        if "application/ld+json" not in content_type:
            msg = "Unexpected content type response from NED NL API."
            raise NedNLError(
                msg,
                {"Content-Type": content_type, "Response": text},
            )

        return text

    async def all_activities(self) -> list[Activity]:
        """Get list of all activities.

        Returns
        -------
            List of all activities.

        """
        response = await self._request("activities")
        return ActivitiesResponse.from_json(response).data

    async def all_classifications(self) -> list[Classification]:
        """Get list of all classifications.

        Returns
        -------
            List of all classifications.

        """
        response = await self._request("classifications")
        return ClassificationsResponse.from_json(response).data

    async def all_granularities(self) -> list[Granularity]:
        """Get list of all granularities.

        Returns
        -------
            List of all granularities.

        """
        response = await self._request("granularities")
        return GranularitiesResponse.from_json(response).data

    async def all_granularity_timezones(self) -> list[GranularityTimezone]:
        """Get list of all granularity timezones.

        Returns
        -------
            List of all granularity timezones.

        """
        response = await self._request("granularity_time_zones")
        return GranularityTimezonesResponse.from_json(response).data

    async def all_points(self) -> list[Point]:
        """Get list of all area points.

        Returns
        -------
            List of all area points.

        """
        response = await self._request("points")
        return PointsResponse.from_json(response).data

    async def all_types(self) -> list[Type]:
        """Get list of all types.

        Returns
        -------
            List of all types.

        """
        response = await self._request("types", params={"itemsPerPage": 100})
        return TypesResponse.from_json(response).data

    async def close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def __aenter__(self) -> Self:
        """Async enter.

        Returns
        -------
            The National Energy Dashboard NL object.

        """
        return self

    async def __aexit__(self, *_exc_info: object) -> None:
        """Async exit.

        Args:
        ----
            _exc_info: Exec type.

        """
        await self.close()
