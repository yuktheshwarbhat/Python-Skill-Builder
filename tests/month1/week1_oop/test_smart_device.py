import pytest

from solutions.month1.week1_oop.device_basic import Device
from solutions.month1.week1_oop.smart_device import SmartDevice


def test_inherits_turn_on() -> None:
    bulb = SmartDevice("smart-bulb")
    assert bulb.status == "OFF"
    bulb.turn_on()
    assert bulb.status == "ON"


def test_adds_connect_wifi() -> None:
    bulb = SmartDevice("smart-bulb")
    assert bulb.is_connected is False
    bulb.connect_wifi("HomeNet")
    assert bulb.ssid == "HomeNet"
    assert bulb.is_connected is True


def test_disconnect_wifi() -> None:
    bulb = SmartDevice("bulb")
    bulb.connect_wifi("HomeNet")
    bulb.disconnect_wifi()
    assert bulb.is_connected is False


def test_parent_init_ran() -> None:
    bulb = SmartDevice("esp32")
    assert bulb.name == "esp32"
    assert bulb.status == "OFF"


def test_isinstance_and_issubclass() -> None:
    bulb = SmartDevice("esp32")
    assert isinstance(bulb, SmartDevice)
    assert isinstance(bulb, Device)
    assert issubclass(SmartDevice, Device)


def test_parent_does_not_get_child_method() -> None:
    assert not hasattr(Device("plain"), "connect_wifi")


def test_empty_ssid_raises() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        SmartDevice("esp32").connect_wifi("   ")


def test_mro() -> None:
    assert SmartDevice.__mro__ == (SmartDevice, Device, object)


def test_polymorphism() -> None:
    def power_up(device: Device) -> str:
        device.turn_on()
        return device.status

    assert power_up(Device("plain")) == "ON"
    assert power_up(SmartDevice("smart")) == "ON"