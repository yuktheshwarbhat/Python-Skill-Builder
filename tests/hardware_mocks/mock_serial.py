"""Fake UART replaces serial.Serial in unit tests."""

from __future__ import annotations


class MockSerial:
    def __init__(self, port: str = "MOCK0", baudrate: int = 115200) -> None:
        self.port = port
        self.baudrate = baudrate
        self.is_open = True
        self.written: list[bytes] = []
        self.responses: dict[str, str] = {}
        self._rx = bytearray()

    def open(self) -> None:
        self.is_open = True

    def close(self) -> None:
        self.is_open = False

    def write(self, data: bytes) -> int:
        if not self.is_open:
            raise OSError("port is closed")
        self.written.append(bytes(data))
        command = data.decode().strip()
        if command in self.responses:
            self._rx.extend((self.responses[command] + "\n").encode())
        return len(data)

    def readline(self) -> bytes:
        index = self._rx.find(b"\n")
        if index == -1:
            data = bytes(self._rx)
            self._rx.clear()
            return data
        data = bytes(self._rx[: index + 1])
        del self._rx[: index + 1]
        return data
