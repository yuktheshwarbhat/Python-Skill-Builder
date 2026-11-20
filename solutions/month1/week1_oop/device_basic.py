from __future__ import annotations

from solutions.month1.week1_oop.device_basic import Device


class SmartDevice(Device):
    """A Device that can join a Wi-Fi network."""

    def __init__(self, name: str, status: str = "OFF") -> None:
        super().__init__(name, status)
        self.ssid: str | None = None

    @property
    def is_connected(self) -> bool:
        """True once the device has joined a network."""
        return self.ssid is not None

    def connect_wifi(self, ssid: str) -> None:
        """Join a Wi-Fi network (mock: records the SSID)."""
        if not ssid.strip():
            raise ValueError("ssid must not be empty")
        self.ssid = ssid

    def __repr__(self) -> str:
        return (
            f"SmartDevice(name={self.name!r}, status={self.status!r}, "
            f"ssid={self.ssid!r})"
        )
