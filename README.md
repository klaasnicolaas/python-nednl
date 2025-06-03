<!-- Banner -->
![alt Banner of the National Energy Dashboard NL package](https://raw.githubusercontent.com/klaasnicolaas/python-nednl/main/assets/header_nednl-min.png)

<!-- PROJECT SHIELDS -->
[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE)

[![GitHub Activity][commits-shield]][commits-url]
[![PyPi Downloads][downloads-shield]][downloads-url]
[![GitHub Last Commit][last-commit-shield]][commits-url]
[![Open in Dev Containers][devcontainer-shield]][devcontainer]

[![Build Status][build-shield]][build-url]
[![Typing Status][typing-shield]][typing-url]
[![Maintainability][maintainability-shield]][maintainability-url]
[![Code Coverage][codecov-shield]][codecov-url]


Asynchronous Python client for [National Energy Dashboard][ned] NL.

## About

A Python package that allows you to retrieve data via the [API][api] of the [National Energy Dashboard][ned]. A data portal with datasets about the gas and electricity providing / consuming in the Netherlands.

## Installation

```bash
pip install nednl
```

### API Key

Before accessing the datasets, it's necessary to create an account on the website of NED. After you have done this, you'll be able to generate a unique API key, granting you access to the datasets.

## Datasets

<!-- TODO: Add a list of datasets that are supported by this package. -->

- All activities
- All classifications
- All granularities
- All granularity timezones
- All points
- All types
- Utilization

Currently there is a limit of 200 requests per 5 minutes.

### Example

An example of how you can query the solar consumption of the Netherlands with a granularity per 10 minutes.

```python
import asyncio

from nednl import NedNL


async def main() -> None:
    """Show example on using this package."""

    async with NedNL("YOUR_API_KEY") as client:
        response = await client.utilization(
            point_id=0,
            type_id=2,
            granularity_id=3,
            granularity_timezone_id=1,
            classification_id=2,
            activity_id=1,
            start_date="2024-03-29",
            end_date="2024-03-30",
        )
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

More examples can be found in the [examples folder](./examples/).

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Setting up development environment

The simplest way to begin is by utilizing the [Dev Container][devcontainer]
feature of Visual Studio Code or by opening a CodeSpace directly on GitHub.
By clicking the button below you immediately start a Dev Container in Visual Studio Code.

[![Open in Dev Containers][devcontainer-shield]][devcontainer]

This Python project relies on [Poetry][poetry] as its dependency manager,
providing comprehensive management and control over project dependencies.

You need at least:

- Python 3.11+
- [Poetry][poetry-install]

### Installation

Install all packages, including all development requirements:

```bash
poetry install
```

_Poetry creates by default an virtual environment where it installs all
necessary pip packages_.

### Pre-commit

This repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. To setup the pre-commit check, run:

```bash
poetry run pre-commit install
```

And to run all checks and tests manually, use the following command:

```bash
poetry run pre-commit run --all-files
```

### Testing

It uses [pytest](https://docs.pytest.org/en/stable/) as the test framework. To run the tests:

```bash
poetry run pytest
```

To update the [syrupy](https://github.com/tophat/syrupy) snapshot tests:

```bash
poetry run pytest --snapshot-update
```

## License

MIT License

Copyright (c) 2024-2025 Klaas Schoute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


<!-- LINKS FROM PLATFORM -->
[ned]: https://ned.nl
[api]: https://ned.nl/nl/handleiding-api

<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://github.com/klaasnicolaas/python-nednl/actions/workflows/tests.yaml/badge.svg
[build-url]: https://github.com/klaasnicolaas/python-nednl/actions/workflows/tests.yaml
[codecov-shield]: https://codecov.io/gh/klaasnicolaas/python-nednl/branch/main/graph/badge.svg?token=B0TL8CNX75
[codecov-url]: https://codecov.io/gh/klaasnicolaas/python-nednl
[commits-shield]: https://img.shields.io/github/commit-activity/y/klaasnicolaas/python-nednl.svg
[commits-url]: https://github.com/klaasnicolaas/python-nednl/commits/main
[devcontainer-shield]: https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode
[devcontainer]: https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/klaasnicolaas/python-nednl
[downloads-shield]: https://img.shields.io/pypi/dm/nednl
[downloads-url]: https://pypistats.org/packages/nednl
[last-commit-shield]: https://img.shields.io/github/last-commit/klaasnicolaas/python-nednl.svg
[license-shield]: https://img.shields.io/github/license/klaasnicolaas/python-nednl.svg
[maintainability-shield]: https://api.codeclimate.com/v1/badges/bd55196e975c3f32591b/maintainability
[maintainability-url]: https://codeclimate.com/github/klaasnicolaas/python-nednl/maintainability
[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg
[project-stage-shield]: https://img.shields.io/badge/project%20stage-experimental-yellow.svg
[pypi]: https://pypi.org/project/nednl/
[python-versions-shield]: https://img.shields.io/pypi/pyversions/nednl
[releases-shield]: https://img.shields.io/github/release/klaasnicolaas/python-nednl.svg
[releases]: https://github.com/klaasnicolaas/python-nednl/releases
[typing-shield]: https://github.com/klaasnicolaas/python-nednl/actions/workflows/typing.yaml/badge.svg
[typing-url]: https://github.com/klaasnicolaas/python-nednl/actions/workflows/typing.yaml

[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
