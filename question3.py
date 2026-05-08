UPPERCASE_LETTERS = 3
DIGITS = 4
LOWERCASE_LETTERS = 2
TOTAL_LENGTH = 9


def ValidateStringFormat(text):
    """Check if the string format is valid."""

    if len(text) != TOTAL_LENGTH:
        return False

    uppercase_characters = text[:UPPERCASE_LETTERS]
    digit_characters = text[UPPERCASE_LETTERS:UPPERCASE_LETTERS + DIGITS]
    lowercase_characters = text[-LOWERCASE_LETTERS:]

    if not uppercase_characters.isupper() or not uppercase_characters.isalpha():
        return False

    if not digit_characters.isdigit():
        return False

    if not lowercase_characters.islower() or not lowercase_characters.isalpha():
        return False

    return True


# check
print(ValidateStringFormat("ABC1234de"))  # True
print(ValidateStringFormat("AB1234de"))   # False