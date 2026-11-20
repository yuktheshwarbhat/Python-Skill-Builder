from solutions.month1.week1_oop.device_basic import Device


def test_turn_on_changes_status() -> None:
    device = Device("esp32")
    assert device.status == "OFF"
    device.turn_on()
    assert device.status == "ON"


def test_name_is_stored() -> None:
    assert Device("stm32").name == "stm32"


def test_turn_off() -> None:
    device = Device("dut")
    device.turn_on()
    device.turn_off()
    assert device.status == "OFF"


def test_turn_on_is_idempotent() -> None:
    device = Device("dut")
    device.turn_on()
    device.turn_on()
    assert device.status == "ON"


def test_instances_are_independent() -> None:
    a, b = Device("a"), Device("b")
    a.turn_on()
    assert a.status == "ON"
    assert b.status == "OFF"


def test_repr() -> None:
    assert repr(Device("esp32")) == "Device(name='esp32', status='OFF')"