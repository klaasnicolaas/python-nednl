"""Asynchronous Python client example for National Energy Dashboard NL."""

from __future__ import annotations

import asyncio

from nednl import Granularity, GranularityTimezone, NedNL


async def main() -> None:
    """Fetch all granularities from the National Energy Dashboard NL."""
    api_key: str = "YOUR_API_KEY"
    async with NedNL(api_key) as client:
        granularities: list[Granularity] = await client.all_granularities()
        granularity_timezones: list[
            GranularityTimezone
        ] = await client.all_granularity_timezones()

        for granularity in granularities:
            print(granularity)

        for item in granularity_timezones:
            print(item)


if __name__ == "__main__":
    asyncio.run(main())
