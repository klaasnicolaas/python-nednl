"""Fixtures for the National Energy Dashboard tests."""

from collections.abc import AsyncGenerator

import pytest
from aiohttp import ClientSession

from nednl import NedNL


@pytest.fixture(name="nednl_client")
async def client() -> AsyncGenerator[NedNL, None]:
    """Create a National Energy Dashboard NL client."""
    async with (
        ClientSession() as session,
        NedNL(api_key="TEST", session=session) as nednl_client,
    ):
        yield nednl_client
