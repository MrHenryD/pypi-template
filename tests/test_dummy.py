import pytest
from parameterized import parameterized

from teenytiny.transform.text import remove_digits


@parameterized.expand(
    [
        ["abc103", "abc"],
    ]
)
@pytest.mark.unit
def test_unit(a: str, b: str):
    assert remove_digits(a) == b


@parameterized.expand(
    [
        ["abc103", "abc"],
    ]
)
@pytest.mark.integration
def test_integration(a: str, b: str):
    assert remove_digits(a) == b


@parameterized.expand(
    [
        ["abc103", "abc"],
    ]
)
@pytest.mark.performance
def test_performance(a: str, b: str):
    assert remove_digits(a) == b
