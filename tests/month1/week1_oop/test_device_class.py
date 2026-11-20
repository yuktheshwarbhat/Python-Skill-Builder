import pytest

from solutions.month1.week1_oop.device_class import BaseDevice, SerialDevice


def test_cannot_instantiate_abstract() -> None:
    with pytest.raises(TypeError):
        BaseDevice("dut")


def test_send_and_receive(mock_serial) -> None:
    dut = SerialDevice("esp32", mock_serial)
    dut.connect()
    assert dut.is_connected
    assert dut.send("AT") == "OK"
    assert mock_serial.written == [b"AT\n"]
    dut.disconnect()
    assert not dut.is_connected


def test_send_without_connect_raises(mock_serial) -> None:
    dut = SerialDevice("stm32", mock_serial)
    with pytest.raises(ConnectionError):
        dut.send("VER")


def test_context_manager_closes(mock_serial) -> None:
    with SerialDevice("esp32", mock_serial) as dut:
        assert dut.send("VER") == "fw-1.2.3"
    assert mock_serial.is_open is False