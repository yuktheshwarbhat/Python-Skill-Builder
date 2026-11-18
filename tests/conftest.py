"""Shared fixtures hardware doubles available to every test."""

from __future__ import annotations

import pytest

from tests.hardware_mocks.mock_serial import MockSerial


@pytest.fixture
def mock_serial() -> MockSerial:
    port = MockSerial()
    port.responses = {"AT": "OK", "VER": "fw-1.2.3", "RESET": "READY"}
    yield port
    port.close()
