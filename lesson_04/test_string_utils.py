import pytest
from string_utils import StringUtils

# def capitilize


@pytest.mark.parametrize("input_text, expected_output", [
 ("test", "Test"),
 ("green table", "Green table"),
 ("223 red 223", "223 Red 223"),
 ("444", "444"),
])
def test_capitilize_positive(input_text, expected_output):
    string = StringUtils()
    assert string.capitilize(input_text) == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
 ("", ""),
 (" ", " "),
 ("/;!!", "/;!!"),
 ("Rest", "Rest"),
])
def test_capitilize_negative(input_text, expected_output):
    string = StringUtils()
    assert string.capitilize(input_text) == expected_output

# def trim


@pytest.mark.parametrize("input_text, expected_output", [
 ("  Test", "Test"),
 ("  123Test", "123Test"),
 (" 123", "123"),
 (" tst 1", "tst 1"),
])
def test_trim_positive(input_text, expected_output):
    string = StringUtils()
    assert string.trim(input_text) == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
 (" ", ""),
 ("", ""),
 ("                                                                   1", "1"),
 (" //!", "//!")
])
def test_trim_negative(input_text, expected_output):
    string = StringUtils()
    assert string.trim(input_text) == expected_output

# def to_list


@pytest.mark.parametrize("input_text, delimeter, expected_output", [
 ("a,b,c,d", ",", ["a", "b", "c", "d"]),
 ("1:2:3:4", ":", ["1", "2", "3", "4"]),
 ("1;b;3;d", ";", ["1", "b", "3", "d"]),
 ("aa.b.ccc.d", ".", ["aa", "b", "ccc", "d"]),
])
def test_to_list_positive(input_text, delimeter, expected_output):
    string = StringUtils()
    assert string.to_list(input_text, delimeter) == expected_output


@pytest.mark.parametrize("input_text, delimeter, expected_output", [
 ("aAbAcAd", "A", ["a", "b", "c", "d"]),
 (" :2: :4", ":", [" ", "2", " ", "4"]),
 ("/;>;@;!", ";", ["/", ">", "@", "!"]),
 ("-0 aAA.b  2.c_____c", ".", ["-0 aAA", "b  2", "c_____c"]),
])
def test_to_list_negative(input_text, delimeter, expected_output):
    string = StringUtils()
    assert string.to_list(input_text, delimeter) == expected_output

# def contains


@pytest.mark.parametrize("input_text, symbol", [
 ("Hello", "l"),
 ("Hello", "H"),
 pytest.param("Hello", "h", marks=pytest.mark.xfail),
 pytest.param("Hello", "O", marks=pytest.mark.xfail),
])
def test_contains_positive(input_text, symbol):
    res = StringUtils()
    assert res.contains(input_text, symbol)


@pytest.mark.parametrize("input_text, symbol", [
 (" Hello", " "),
 ("", ""),
 (" H 0", "0"),
 ("//]]", "]"),
])
def test_contains_negative(input_text, symbol):
    res = StringUtils()
    assert res.contains(input_text, symbol)

# def delete_symbol


@pytest.mark.parametrize("input_text, symbol, expected_output", [
 ("tessst", "sss", "tet"),
 ("te11", "11", "te"),
 ("1111t1111", "t", "11111111"),
 ("1 t", " ", "1t"),
])
def test_delete_symbol_positive(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.delete_symbol(input_text, symbol) == expected_output


@pytest.mark.parametrize("input_text, symbol, expected_output", [
 (" ", "", " "),
 ("te11", "te11", ""),
 (" ", " ", ""),
 ("sets", "s", "et"),
])
def test_delete_symbol_negative(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.delete_symbol(input_text, symbol) == expected_output


# def starts_with


@pytest.mark.parametrize("input_text, symbol", [
 ("Hello", "H"),
 pytest.param("Hello", "e", marks=pytest.mark.xfail),
 ("123 H", "1"),
 ("133", "1"),
])
def test_starts_with_positive(input_text, symbol):
    string = StringUtils()
    assert string.starts_with(input_text, symbol)


@pytest.mark.parametrize("input_text, symbol", [
 ("", ""),
 (" Hello", " "),
 ("_123 H", "_"),
 ("1", "1"),
])
def test_starts_with_negative(input_text, symbol):
    string = StringUtils()
    assert string.starts_with(input_text, symbol)

# def starts_with


@pytest.mark.parametrize("input_text, symbol", [
 ("Hello", "o"),
 ("123", "3"),
 ("1", "1"),
 pytest.param("Hello", "l", marks=pytest.mark.xfail),
])
def test_end_with_positive(input_text, symbol):
    string = StringUtils()
    assert string.end_with(input_text, symbol)


@pytest.mark.parametrize("input_text, symbol", [
 ("1", "1"),
 ("Hello ", " "),
 ("_123_", "_"),
 ("", ""),
])
def test_end_with_negative(input_text, symbol):
    string = StringUtils()
    assert string.end_with(input_text, symbol)

# def is_empty


@pytest.mark.parametrize("input_text", [
 (""),
 (" "),
])
def test_is_empty_positive(input_text):
    string = StringUtils()
    assert string.is_empty(input_text)


@pytest.mark.xfail
@pytest.mark.parametrize("input_text", [
 ("123"),
 ("Abc"),
])
def test_is_empty_negative(input_text):
    string = StringUtils()
    assert string.is_empty(input_text)

# def list_to_string


@pytest.mark.parametrize("list, joiner, expected_output", [
    ([1, 2, 3, 4], ".", "1.2.3.4"),
    (["born", "to", "win"], "-", "born-to-win"),
    (["BAD", "day"], " ", "BAD day"),
])
def test_list_to_string_positive(list, joiner, expected_output):
    res = StringUtils().list_to_string(list, joiner)
    assert res == expected_output


@pytest.mark.parametrize("list, joiner, expected_output", [
    ([], ".", ""),
    ([" ", " ", " "], "-", " - - "),
    (["", ""], " ", " "),
])
def test_list_to_string_negative(list, joiner, expected_output):
    res = StringUtils().list_to_string(list, joiner)
    assert res == expected_output
