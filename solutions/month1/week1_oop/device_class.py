"""Q31/Q39/Q44 OOP pillars applied to a firmware test bench."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Device(ABC):
    """Abstract device under test."""

    def __init__(self, name: str, transport: Any | None = None) -> None:
        self.name = name
        self._transport = transport
        self._connected = False

    @property
    def is_connected(self) -> bool:
        return self._connected

    def connect(self) -> Device:
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

    def __enter__(self) -> Device:
        return self.connect()

    def __exit__(self, *exc) -> bool:
        self.disconnect()
        return False


class SerialDevice(Device):
    """Line-oriented CLI device (ESP32 / STM32 shell)."""

    def send(self, command: str) -> str:
        if not self.is_connected:
            raise ConnectionError(f"{self.name} is not connected")
        self._transport.write((command + "\n").encode())
        return self._transport.readline().decode().strip()
