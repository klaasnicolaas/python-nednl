"""Asynchronous Python client example for National Energy Dashboard NL."""

import asyncio

from nednl import NedNL


async def main() -> None:
    """Fetch all activities from the National Energy Dashboard NL."""
    api_key: str = "YOUR_API_KEY"
    async with NedNL(api_key) as client:
        activities = await client.all_activities()

        for item in activities:
            print(item)


if __name__ == "__main__":
    asyncio.run(main())
