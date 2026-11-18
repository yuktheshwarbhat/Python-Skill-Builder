"""Tests for the Device abstraction no hardware required."""

import pytest

from solutions.month1.week1_oop.device_class import Device, SerialDevice


def test_abstract_class_cannot_instantiate() -> None:
    with pytest.raises(TypeError):
        Device("dut")


def test_send_and_receive(mock_serial) -> None:
    with SerialDevice("esp32", mock_serial) as dut:
        assert dut.is_connected
        assert dut.send("AT") == "OK"
        assert mock_serial.written == [b"AT\n"]
    assert not dut.is_connected
    assert not mock_serial.is_open


def test_send_without_connect_raises(mock_serial) -> None:
    dut = SerialDevice("stm32", mock_serial)
    with pytest.raises(ConnectionError):
        dut.send("VER")
