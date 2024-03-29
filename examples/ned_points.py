"""Asynchronous Python client example for National Energy Dashboard NL."""

import asyncio

from nednl import NedNL


async def main() -> None:
    """Fetch all area points from the National Energy Dashboard NL."""
    api_key: str = "YOUR_API_KEY"
    async with NedNL(api_key) as client:
        points = await client.all_points()

        for item in points:
            print(item)


if __name__ == "__main__":
    asyncio.run(main())
