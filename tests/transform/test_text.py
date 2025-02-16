from parameterized import parameterized

from teenytiny.transform import text


@parameterized.expand(
    [
        ["100-100-100", "--"],
        ["100a100b100c", "abc"],
    ]
)
def test_remove_digits(a: str, b: str):
    assert text.remove_digits(a) == b


@parameterized.expand(
    [
        ["100-100-100", "100100100"],
        ["aaa-bbb-ccc", "aaabbbccc"],
    ]
)
def test_remove_special_characters(a: str, b: str):
    return text.remove_special_characters(a) == b
