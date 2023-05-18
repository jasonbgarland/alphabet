import random
import string

from api.service.alphabet import string_contains_alphabet

ALPHABET_STRING = "abcdefghijklmnopqrstuvwxyz"
def generate_random_str(
    length: int,
    uppercase=True,
    digits=True,
    special=True,
    whitespace=True,
    unicode=True,
):
    # construct character choices
    letters = string.ascii_lowercase
    if uppercase:
        letters = letters + string.ascii_uppercase
    if digits:
        letters = letters + string.digits
    if special:
        letters = letters + string.punctuation
    if whitespace:
        letters = letters + string.whitespace
    if unicode:
        letters = letters + "\u03B1\u03A9"  # just a small subset

    return "".join(random.choice(letters) for i in range(length))


class TestStringContainsAlphabet:
    def test_string_contains_alphabet_returns_true(self):
        test_string = ALPHABET_STRING
        assert string_contains_alphabet(test_string) is True

    def test_string_does_not_contain_alphabet_returns_false(self):
        test_string = "defghijklmnopqrstuvwxyz"
        assert string_contains_alphabet(test_string) is False

    def test_string_contains_alphabet_empty_string_return_false(self):
        test_string = ""
        assert string_contains_alphabet(test_string) is False

    def test_string_contains_alphabet_order_not_important(self):
        test_string = "xambefghijklnopqrstuvwdyzc"
        assert string_contains_alphabet(test_string) is True

    def test_string_contains_alphabet_case_not_important(self):
        test_string = "ABCDefghijklmnopqrstuvwXYZ"
        assert string_contains_alphabet(test_string) is True

    def test_string_contains_alphabet_digits_ok(self):
        test_string = "1a1b1c2d3e4f56g67h8i9jklmn000opqrstuvwxyz"
        assert string_contains_alphabet(test_string) is True

    def test_string_contains_alphabet_special_characters_ok(self):
        test_string = "!!!abc?defgh$ijk&lm*nop)(qrst><uv@wxyz"
        assert string_contains_alphabet(test_string) is True

    def test_string_contains_alphabet_unicode_characters_ok(self):
        test_string = "\u03B1abcdefghijklmnopqrstuvwxyz\u03A9"
        assert string_contains_alphabet(test_string) is True

    def test_string_contains_alphabet_whitepsace_characters_ok(self):
        test_string = "    abcdefg\t\t\thijklmn\nopqrstuvwxyz"
        assert string_contains_alphabet(test_string) is True

    def test_string_contains_alphabet_all_the_things_returns_true(self):
        test_string = "11!lmnopqrstuvwXYZabcdefghijk\u03A9\n"
        assert string_contains_alphabet(test_string) is True

    def test_string_contains_alphabet_large_string_returns_true(self):
        test_string = generate_random_str(1000)
        assert string_contains_alphabet(test_string) is True

    def test_string_contains_alphabet_really_large_string_returns_true(self):
        # not very probable, but make sure to include all the letters at the end so we have a consistent test result
        test_string = generate_random_str(100000) + ALPHABET_STRING
        assert string_contains_alphabet(test_string) is True

