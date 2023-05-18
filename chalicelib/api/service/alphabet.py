def string_contains_alphabet(string_to_check: str) -> bool:
    """
    Returns whether the given string contains every letter of the alphabet. This is a case-insensitive check.
    :param string_to_check: The string to check. The string can be a mixture of upper and lower case, numbers,
    special characters etc.
    :return: True if the string contains at least one character from every letter of the alphabet, False otherwise.
    """
    letter_count = {}
    missing = 26

    for character in string_to_check:
        if character.isalpha():
            current_count = letter_count.get(character.lower(), 0)

            if current_count == 0:
                missing = missing - 1

                # Stop right away if we've found the last character
                if missing == 0:
                    return True

            letter_count[character.lower()] = current_count + 1

    return False
