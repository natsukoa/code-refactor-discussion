import pytest
import fizzbuzz


@pytest.mark.parametrize(
    ["test_input", "expected"],
    [
        (1, "1"),
        (2, "2"),
        (3, "Fizz"),
        (6, "Fizz"),
        (5, "Buzz"),
        (10, "Buzz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
    ],
)
def test_fizzbuzz(test_input, expected):
    assert fizzbuzz.fizz_buzz(test_input) == expected
