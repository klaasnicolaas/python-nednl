"""Test the models for National Energy Dashboard NL."""

from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from nednl import NedNL

from . import load_fixtures


async def test_activities_data(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    nednl_client: NedNL,
) -> None:
    """Test activities data is handled correctly."""
    aresponses.add(
        "api.ned.nl",
        "/v1/activities",
        "GET",
        aresponses.Response(
            status=200,
            content_type="application/ld+json",
            body=load_fixtures("activities.json"),
        ),
    )
    response = await nednl_client.all_activities()
    assert response == snapshot


async def test_classifications_data(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    nednl_client: NedNL,
) -> None:
    """Test classifications data is handled correctly."""
    aresponses.add(
        "api.ned.nl",
        "/v1/classifications",
        "GET",
        aresponses.Response(
            status=200,
            content_type="application/ld+json",
            body=load_fixtures("classifications.json"),
        ),
    )
    response = await nednl_client.all_classifications()
    assert response == snapshot


async def test_granularities_data(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    nednl_client: NedNL,
) -> None:
    """Test granularities data is handled correctly."""
    aresponses.add(
        "api.ned.nl",
        "/v1/granularities",
        "GET",
        aresponses.Response(
            status=200,
            content_type="application/ld+json",
            body=load_fixtures("granularities.json"),
        ),
    )
    response = await nednl_client.all_granularities()
    assert response == snapshot


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


async def test_types_data(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    nednl_client: NedNL,
) -> None:
    """Test types data is handled correctly."""
    aresponses.add(
        "api.ned.nl",
        "/v1/types",
        "GET",
        aresponses.Response(
            status=200,
            content_type="application/ld+json",
            body=load_fixtures("types.json"),
        ),
    )
    response = await nednl_client.all_types()
    assert response == snapshot
