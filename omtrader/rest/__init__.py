"""
OMTrader REST API

This module provides access to the OMTrader REST API functionality.
"""

from .client import RESTClient
from .exceptions import (
    ApiException,
    ApiTypeError,
    ApiValueError,
    ApiKeyError,
    ApiAttributeError,
    OpenApiException
)

__all__ = [
    "RESTClient",
    "ApiException",
    "ApiTypeError", 
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "OpenApiException"
]
