"""Q31 - Simple concrete Device: name, status, turn_on()."""

from __future__ import annotations


class Device:
    """A simple on/off device under test."""

    def __init__(self, name: str, status: str = "OFF") -> None:
        self.name = name
        self.status = status

    def turn_on(self) -> None:
        """Switch the device on."""
        self.status = "ON"

    def turn_off(self) -> None:
        """Switch the device off."""
        self.status = "OFF"

    def __repr__(self) -> str:
        return f"Device(name={self.name!r}, status={self.status!r})"
