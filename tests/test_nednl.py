"""Basic tests for National Energy Dashboard NL."""

# pylint: disable=protected-access
import asyncio
from unittest.mock import patch

import pytest
from aiohttp import ClientError, ClientResponse, ClientSession
from aresponses import Response, ResponsesMockServer

from nednl import NedNL
from nednl.exceptions import (
    NedNLConnectionError,
    NedNLError,
)

from . import load_fixtures


async def test_json_request(
    aresponses: ResponsesMockServer,
    nednl_client: NedNL,
) -> None:
    """Test JSON response is handled correctly."""
    aresponses.add(
        "api.ned.nl",
        "/v1/test",
        "GET",
        aresponses.Response(
            status=200,
            content_type="application/ld+json",
            body=load_fixtures("points.json"),
        ),
    )
    response = await nednl_client._request("test")
    assert response is not None
    await nednl_client.close()


async def test_internal_session(aresponses: ResponsesMockServer) -> None:
    """Test internal session is created and closed."""
    aresponses.add(
        "api.ned.nl",
        "/v1/test",
        "GET",
        aresponses.Response(
            status=200,
            content_type="application/ld+json",
            body=load_fixtures("points.json"),
        ),
    )
    async with NedNL(api_key="TEST") as client:
        await client._request("test")


async def test_timeout(aresponses: ResponsesMockServer) -> None:
    """Test timeout error handling."""

    # Faking a timeout by sleeping
    async def response_handler(_: ClientResponse) -> Response:
        await asyncio.sleep(0.2)
        return aresponses.Response(
            body="Goodmorning!",
        )

    aresponses.add(
        "api.ned.nl",
        "/v1/test",
        "GET",
        response_handler,
    )

    async with ClientSession() as session:
        client = NedNL(api_key="Key", session=session, request_timeout=0.1)
        with pytest.raises(NedNLConnectionError):
            await client._request("test")


async def test_content_type(
    aresponses: ResponsesMockServer,
    nednl_client: NedNL,
) -> None:
    """Test content type error handling."""
    aresponses.add(
        "api.ned.nl",
        "/v1/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "blabla/blabla"},
        ),
    )
    with pytest.raises(NedNLError):
        assert await nednl_client._request("test")


async def test_client_error() -> None:
    """Test request client error handling."""
    async with ClientSession() as session:
        client = NedNL(api_key="Key", session=session)
        with (
            patch.object(
                session,
                "request",
                side_effect=ClientError(),
            ),
            pytest.raises(NedNLConnectionError),
        ):
            assert await client._request("test")


async def test_status_404(
    aresponses: ResponsesMockServer,
    nednl_client: NedNL,
) -> None:
    """Test response status 404 handling."""
    aresponses.add(
        "api.ned.nl",
        "/v1/test",
        "GET",
        aresponses.Response(
            status=404,
        ),
    )
    with pytest.raises(NedNLConnectionError):
        assert await nednl_client._request("test")
