"""
This is my submission for the coding example at:
https://www.hackerrank.com/challenges/validating-credit-card-number/problem
"""
import re


class InputIntegerException(Exception):
    pass


def verify_credit_card_validity(credit_card_number: str) -> str:
    regex_credit_card_number = re.match(
        "([4-6]{1}[\d]{3}\-?\d{4}\-?\d{4}\-?\d{4})", credit_card_number.strip('`~!@#$%^&*()_=+\\/,<.>/?|[]{}'))
    return_message = 'Valid'

    if not regex_credit_card_number:
        return_message = 'Invalid'
    else:
        if len(regex_credit_card_number.string.replace('-', '')) != 16:
            return_message = 'Invalid'

        if regex_credit_card_number.string.startswith(' ') or regex_credit_card_number.string.endswith(' '):
            return_message = 'Invalid'

        digit_counter = {}
        last_character = regex_credit_card_number.string[0]
        for character in regex_credit_card_number.string[1:]:
            if not character.isdigit():
                continue
            if int(last_character) == int(character):
                if character not in digit_counter:
                    digit_counter[character] = 2
                else:
                    digit_counter[character] += 1
                if digit_counter[character] >= 4:
                    return 'Invalid'
            last_character = character

    return return_message


if __name__ == "__main__":
    try:
        input_line_count = int(input())  # Our first input is the count of inputs to test.
    except ValueError:
        raise InputIntegerException('input() must be an integer matching the number of credit cards to check.')
    raw_output = ''

    for i in range(input_line_count):  # The remaining inputs are the credit card numbers.
        separator = '\n'
        if i == input_line_count - 1:  # Last one in the string doesn't need a linebreak.
            separator = ''
        input_string = input()
        raw_output += verify_credit_card_validity(input_string) + separator
    print(raw_output)
