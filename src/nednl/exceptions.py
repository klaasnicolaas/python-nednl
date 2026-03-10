"""Asynchronous Python client for National Energy Dashboard NL."""

from __future__ import annotations

from typing import Any


class NedNLError(Exception):
    """Generic NED NL exception."""

    def __init__(self, data: dict[str, Any] | str) -> None:
        """Initialize the exception.

        Args:
        ----
            data: Either an error response dict or a plain error message string.

        """
        if isinstance(data, dict):
            # Support both Hydra format and simple message format
            message = (
                data.get("hydra:description") or data.get("message") or "Unknown error"
            )
            super().__init__(message)
        else:
            super().__init__(data)


class NedNLConnectionError(NedNLError):
    """NED NL connection exception."""


class NedNLAuthenticationError(NedNLError):
    """NED NL authentication exception."""


class NedNLTimeoutError(NedNLConnectionError):
    """NED NL timeout exception."""


class NedNLRateLimitError(NedNLError):
    """NED NL rate limit exception (HTTP 429)."""


class NedNLClientError(NedNLError):
    """NED NL client error exception (HTTP 4xx)."""


class NedNLNotFoundError(NedNLClientError):
    """NED NL not found exception (HTTP 404)."""


class NedNLValidationError(NedNLClientError):
    """NED NL validation error exception (HTTP 400)."""


class NedNLServerError(NedNLError):
    """NED NL server error exception (HTTP 5xx)."""
