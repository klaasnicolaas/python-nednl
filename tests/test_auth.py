"""Tests for the NedNL authentication."""

# pylint: disable=protected-access
import pytest
from aiohttp import ClientSession
from aresponses import ResponsesMockServer

from nednl import NedNL
from nednl.exceptions import NedNLAuthenticationError

from . import load_fixtures


async def test_missing_api_key(aresponses: ResponsesMockServer) -> None:
    """Test missing API key."""
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
    async with ClientSession() as session:
        client = NedNL(
            api_key="",
            session=session,
        )
        with pytest.raises(NedNLAuthenticationError):
            await client.all_points()


async def test_status_403(
    aresponses: ResponsesMockServer,
    nednl_client: NedNL,
) -> None:
    """Test response status 403 handling."""
    aresponses.add(
        "api.ned.nl",
        "/v1/test",
        "GET",
        aresponses.Response(
            status=403,
        ),
    )
    with pytest.raises(NedNLAuthenticationError):
        assert await nednl_client._request("test")
