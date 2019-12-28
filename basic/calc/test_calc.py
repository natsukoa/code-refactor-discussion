import pytest
import calc


@pytest.mark.parametrize(
    ["test_input", "expected"], [([10, 5], (15, 5)), ([3, 10], (13, -7)),],
)
def test_calc(test_input, expected):
    assert calc.calc(*test_input) == expected
