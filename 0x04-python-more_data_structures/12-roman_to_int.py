#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    number = 0
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    for i, c in enumerate(roman_string):
        if (i < len(roman_string) - 1 and
                numerals[roman_string[i+1]] > numerals[c]):
            number -= numerals[c]
        else:
            number += numerals[c]

    return number
