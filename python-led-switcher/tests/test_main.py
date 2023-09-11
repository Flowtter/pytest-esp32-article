import pytest
from src.main import LedSwitcher

@pytest.fixture
def ledSwitcher():
    return LedSwitcher(green_led_pin=1, red_led_pin=2)

def test_pinAssignments(ledSwitcher):
    assert (ledSwitcher.greenLed.pinForTesting == 1)
    assert (ledSwitcher.redLed.pinForTesting == 2)


def test_green(ledSwitcher):
    ledSwitcher.green()
    assert ledSwitcher.greenLed.value() == 1
    assert ledSwitcher.redLed.value() == 0


def test_red(ledSwitcher):
    ledSwitcher.red()
    assert ledSwitcher.greenLed.value() == 0
    assert ledSwitcher.redLed.value() == 1
