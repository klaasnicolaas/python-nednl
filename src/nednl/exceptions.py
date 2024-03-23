"""Asynchronous Python client for National Energy Dashboard NL."""


class NedNLError(Exception):
    """Generic NED NL exception."""


class NedNLConnectionError(NedNLError):
    """NED NL connection exception."""


class NedNLAuthenticationError(NedNLError):
    """NED NL authentication exception."""
