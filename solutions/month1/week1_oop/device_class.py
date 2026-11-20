from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseDevice(ABC):
    """Abstract DUT that talks over a transport."""

    def __init__(self, name: str, transport: Any | None = None) -> None:
        self.name = name
        self._transport = transport
        self._connected = False

    @property
    def is_connected(self) -> bool:
        return self._connected

    def connect(self) -> BaseDevice:
        if self._transport is not None:
            self._transport.open()
        self._connected = True
        return self

    def disconnect(self) -> None:
        if self._transport is not None:
            self._transport.close()
        self._connected = False

    @abstractmethod
    def send(self, command: str) -> str:
        """Send a command, return the response."""

    def __enter__(self) -> BaseDevice:
        return self.connect()

    def __exit__(self, *exc) -> bool:
        self.disconnect()
        return False


class SerialDevice(BaseDevice):
    """Line-oriented CLI device (ESP32 / STM32 shell)."""

    def send(self, command: str) -> str:
        if not self.is_connected:
            raise ConnectionError(f"{self.name} is not connected")
        self._transport.write((command + "\n").encode())
        return self._transport.readline().decode().strip()