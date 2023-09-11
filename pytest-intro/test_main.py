import pytest
from main import FruitSalad

@pytest.fixture
def fruit_list():
    return ["Apple", "Banana", "Orange"]


@pytest.fixture
def fruit_salad(fruit_list):
    return FruitSalad(fruit_list)


def test_immutable_fixture(fruit_list):
    original_fruits = fruit_list.copy()
    fruit_list.pop()
    assert fruit_list != original_fruits


def test_fruit_salad(fruit_salad):
    result = fruit_salad.mix()
    assert "Apple" in result
    assert "Banana" in result
    assert "Orange" in result


@pytest.mark.parametrize(
    "other_fruit_list, expected",
    [(["Apple", "Banana"], "Apple Banana"), (["Orange", "Cherry"], "Orange Cherry")],
)
def test_mix_function(other_fruit_list, expected):
    fs = FruitSalad(other_fruit_list)
    result = fs.mix()
    assert result == expected
