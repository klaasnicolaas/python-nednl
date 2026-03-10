"""Basic tests for National Energy Dashboard NL."""

# pylint: disable=protected-access
import asyncio
from unittest.mock import patch

import pytest
from aiohttp import ClientError, ClientResponse, ClientSession
from aresponses import Response, ResponsesMockServer

from nednl import NedNL
from nednl.exceptions import (
    NedNLClientError,
    NedNLConnectionError,
    NedNLError,
    NedNLNotFoundError,
    NedNLRateLimitError,
    NedNLServerError,
    NedNLTimeoutError,
    NedNLValidationError,
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
        with pytest.raises(NedNLTimeoutError):
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


@pytest.mark.parametrize(
    ("status", "fixture", "exception"),
    [
        (400, "error_400.json", NedNLValidationError),
        (404, "error_404.json", NedNLNotFoundError),
        (418, None, NedNLClientError),
        (429, "error_429.json", NedNLRateLimitError),
        (500, "error_500.json", NedNLServerError),
    ],
)
async def test_http_error_status(
    aresponses: ResponsesMockServer,
    nednl_client: NedNL,
    status: int,
    fixture: str | None,
    exception: type[Exception],
) -> None:
    """Test HTTP error status handling."""
    body = (
        load_fixtures(fixture) if fixture else f'{{"message": "HTTP {status} error"}}'
    )
    aresponses.add(
        "api.ned.nl",
        "/v1/test",
        "GET",
        aresponses.Response(
            status=status,
            content_type="application/ld+json",
            body=body,
        ),
    )
    with pytest.raises(exception):
        assert await nednl_client._request("test")


async def test_invalid_json_error_response(
    aresponses: ResponsesMockServer,
    nednl_client: NedNL,
) -> None:
    """Test error response with invalid JSON."""
    aresponses.add(
        "api.ned.nl",
        "/v1/test",
        "GET",
        aresponses.Response(
            status=404,
            content_type="application/ld+json",
            body="This is not valid JSON",
        ),
    )
    with pytest.raises(NedNLNotFoundError):
        assert await nednl_client._request("test")
