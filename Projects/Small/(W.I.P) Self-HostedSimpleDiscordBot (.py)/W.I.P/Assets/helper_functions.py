"""
This module contains universal functions made specifically for this project.
"""

from base64 import b64encode, b64decode
from re import findall
from math import ceil


def b64encode_utf8(my_bytes: bytes) -> str:
    """This is a simple function to convert some bytes into a readable string.
    :param my_bytes: These are the bytes to be converted into a string.
    :return: The bytes encoded with BASE64 and decoded with utf-8 into a readable \
    string.
    """
    return b64encode(my_bytes).decode('utf-8')


def my_b64decode(my_string: str) -> bytes:
    """This is a simple function to convert bytes encoded with BASE64 and decoded \
    with UTF-8 into a string, back into bytes.
    :param my_string: This is the string to convert back into bytes.
    :return: The string decoded with BASE64 back into bytes.
    """
    return b64decode(my_string)


def find_ints_in_string(to_match: str) -> list:
    """
    :param to_match: The string to find numbers in.
    :return: A list of all found ints.
    """

    pattern = r'\d\d*'

    return [int(match) for match in findall(pattern, to_match)]


def remove_non_letters_in_string(my_string: str) -> str:
    """
    :param my_string: String to remove special characters from.
    :return: The passed string without special characters.
    """
    return ''.join(findall(r'[\w\s]+', my_string))


def predictable_shuffle_string(my_str: str) -> str:
    """
    This function was written to shuffle a string without any randomness. It was \
    designed to make the inputted string be hard to recreate by an average Joe.
    :param my_str: This is the string to be shuffled:
    :return: The shuffled string.
    """

    my_str: str = my_str[::-1]

    def recursive_unsort(my_slice: str) -> str:
        my_slice_len: int = len(my_slice)

        if my_slice_len <= 2:
            return my_slice

        new_slice: str = ''

        for i in range(ceil(my_slice_len / 2)):
            new_slice += my_slice[i:i + 1] + my_slice[-i - 1]

        new_slice_len: int = len(new_slice)

        if len(new_slice) > my_slice_len:
            new_slice: str = new_slice[:-1]
            new_slice_len: int = len(new_slice)

        new_slice_half_pos: int = ceil(new_slice_len/2)

        half1 = recursive_unsort(new_slice[:new_slice_half_pos])
        half2 = recursive_unsort(new_slice[new_slice_half_pos:])

        return half1 + half2

    for _ in range(len(my_str)):
        my_str: str = recursive_unsort(my_str)

    return recursive_unsort(my_str)
