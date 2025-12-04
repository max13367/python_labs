import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


# ------------------------- normalize -------------------------


@pytest.mark.parametrize(
    "src,expected",
    [
        ("HeLlo WOrld", "hello world"),
        ("", ""),
        ("TEST", "test"),
        ("Hello\tWorld", "hello world"),
        ("ПРивет\nМИр\t\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
    ],
)
def test_normalize_parametrized(src, expected):
    assert normalize(src) == expected

def test_normalize_wrong_type():
    with pytest.raises(TypeError):
        normalize(123)


def test_normalize_control_characters_removed():
    raw = "Hello\tWorld\nTest"
    out = normalize(raw)

    assert "\t" not in out
    assert "\n" not in out
    assert "  " not in out


def test_normalize_yo_to_e():
    text = "ёжик ёлка Ёлка Ёжик"
    assert normalize(text) == "ежик елка елка ежик"


# ------------------------- tokenize -------------------------


@pytest.mark.parametrize(
    "src,expected",
    [
        ("hello world test", ["hello", "world", "test"]),
        ("", []),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("Meow_meow-", ["Meow_meow"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
    ],
)
def test_tokenize_parametrized(src, expected):
    assert tokenize(src) == expected


# ------------------------- count_freq -------------------------


@pytest.mark.parametrize(
    "tokens,expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        ([" "], {" ": 1}),
        (
            ["bb", "aa", "bb", "aa", "cc"],
            {"aa": 2, "bb": 2, "cc": 1},
        ),
        ([], {}),
        (
            ["a", "a", "b", "b", "c", "c", "1", "1", "f", "f", "f"],
            {"1": 2, "a": 2, "b": 2, "c": 2, "f": 3},
        ),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


# ------------------------- top_n -------------------------


def test_top_n_basic():
    freq = {"apple": 5, "banana": 3, "orange": 4, "grape": 2}
    out = top_n(freq, 3)
    assert out == [("apple", 5), ("orange", 4), ("banana", 3)]


def test_top_n_tie_breaker_alphabetical():
    freq = {"banana": 3, "apple": 3, "cherry": 3, "date": 2}
    out = top_n(freq, 3)
    assert out == [("apple", 3), ("banana", 3), ("cherry", 3)]


def test_top_n_request_more_than_available():
    freq = {"apple": 3, "banana": 2}
    out = top_n(freq, 5)
    assert out == [("apple", 3), ("banana", 2)]


def test_top_n_zero_returns_empty():
    assert top_n({"apple": 3, "banana": 2}, 0) == []


@pytest.mark.parametrize(
    "freq,n,expected",
    [
        ({}, 5, []),
        ({"a": 1}, 0, []),
        ({"a": 2, "b": 1}, 2, [("a", 2), ("b", 1)]),
        ({"b": 1, "a": 1}, 2, [("a", 1), ("b", 1)]),
    ],
)
def test_top_n_parametrized(freq, n, expected):
    assert top_n(freq, n) == expected
