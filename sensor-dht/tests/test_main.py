import pytest
from src.main import App


@pytest.fixture
def app():
    return App(sendor_pin=4, green_led_pin=2)


def test_app(app):
    assert app.led_switcher.greenLed.value() == 0
    temperature, humidity = app.run()
    assert temperature == 26.5
    assert humidity == 48.0
    assert app.led_switcher.greenLed.value() == 1
