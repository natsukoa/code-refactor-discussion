import pytest
import admission_fee


@pytest.mark.parametrize(
    ["test_input", "expected"],
    [
        ([5, {}], 100),
        ([15, {"student": True}], 200),
        ([30, {}], 200),
        ([30, {"citizen": False}], 500),
        ([18, {"student": True, "citizen": False}], 300),
    ],
)
def test_admission_fee(test_input, expected):
    assert admission_fee.calc_admission_fee(test_input[0], **test_input[1]) == expected
