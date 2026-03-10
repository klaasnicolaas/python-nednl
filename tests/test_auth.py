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


@pytest.mark.parametrize(
    ("status", "fixture"),
    [
        (401, "error_401.json"),
        (403, "error_403.json"),
    ],
)
async def test_authentication_error(
    aresponses: ResponsesMockServer,
    nednl_client: NedNL,
    status: int,
    fixture: str,
) -> None:
    """Test authentication error handling."""
    aresponses.add(
        "api.ned.nl",
        "/v1/test",
        "GET",
        aresponses.Response(
            status=status,
            content_type="application/ld+json",
            body=load_fixtures(fixture),
        ),
    )
    with pytest.raises(NedNLAuthenticationError):
        assert await nednl_client._request("test")
