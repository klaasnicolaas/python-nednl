"""Test the models for National Energy Dashboard NL."""

from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from nednl import NedNL

from . import load_fixtures


async def test_points_data(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    nednl_client: NedNL,
) -> None:
    """Test points data is handled correctly."""
    aresponses.add(
        "api.ned.nl",
        "/v1/points",
        "GET",
        aresponses.Response(
            status=200,
            content_type="application/ld+json",
            body=load_fixtures("points.json"),
        ),
    )
    response = await nednl_client.all_points()
    assert response == snapshot
