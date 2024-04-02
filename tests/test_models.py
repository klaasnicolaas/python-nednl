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


async def test_granularity_timezones_data(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    nednl_client: NedNL,
) -> None:
    """Test granularity timezones data is handled correctly."""
    aresponses.add(
        "api.ned.nl",
        "/v1/granularity_time_zones",
        "GET",
        aresponses.Response(
            status=200,
            content_type="application/ld+json",
            body=load_fixtures("granularity_timezones.json"),
        ),
    )
    response = await nednl_client.all_granularity_timezones()
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


async def test_utilizations_data(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    nednl_client: NedNL,
) -> None:
    """Test utilizations data is handled correctly."""
    aresponses.add(
        "api.ned.nl",
        "/v1/utilizations",
        "GET",
        aresponses.Response(
            status=200,
            content_type="application/ld+json",
            body=load_fixtures("utilizations.json"),
        ),
    )
    response = await nednl_client.utilization(
        point_id=0,
        type_id=2,
        granularity_id=3,
        granularity_timezone_id=1,
        classification_id=2,
        activity_id=1,
        start_date="2024-03-29",
        end_date="2024-03-30",
    )
    assert response == snapshot
