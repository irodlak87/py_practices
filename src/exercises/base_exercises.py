"""

Find the index of a substring within a string.
Given a range of numbers, find all numbers within the range that are perfect squares.

Variation of the number of islands question on Leetcode.

Count the moves needed to flip a set of dice to all show the same number.

You have an array of bulbs and corresponding switches, given a sequence of switch actions
count the instances of all the bulbs being on.

You have a non-empty array of numbers, find the deepest pit and return the depth.
A pit is defined as a sequence of decreasing then increasing numbers in the array.



"""
from typing import List
import numpy as np
import pandas as pd

def find_substring_idx(string: str, substring: str) -> int:
    """ returns the first idx of a substring which can be found in a string. It will return None if the substring
        cannot be found
    """
    first_search_char = substring[0]
    len_substring = len(substring)

    for i, char in enumerate(string):
        if char == first_search_char:
            if string[i:i+len_substring] == substring:
                return i

    return None


def find_perfect_squares(start: int, end: int) -> np.array:
    """ function find numbers which are perfect squares in a given range"""

    def np_is_integer(arr: np.array) -> np.array:
        return np.equal(np.mod(arr, 1), 0)

    all_numbers = np.arange(start, end+1)
    square_roots = np.sqrt(all_numbers)
    return all_numbers[np_is_integer(square_roots)]

def find_deepest_pit(numbers) -> np.array:
    """ """
    numbers = np.array(numbers)

    def np_shift(xs, n):
        e = np.empty_like(xs)
        if n >= 0:
            e[:n] = np.nan
            e[n:] = xs[:-n]
        else:
            e[n:] = np.nan
            e[:n] = xs[-n:]
        return e

    if numbers.size < 3:
        # easy case
        if numbers[1] < numbers[0] and numbers[2] > numbers[1]:
            return 3
        else:
            return 0
    else:

        diffs = np.ediff1d(np.array(numbers))
        slopes = np.empty_like(diffs, dtype=np.float64)
        slopes[diffs > 0.0] = 1
        slopes[diffs <= 0.0] = 0

        deriv = np_shift(np.ediff1d(slopes), -1)
        deriv[-1] = -1 if numbers[-2] < numbers[-1] else 0

        tops = np.zeros(numbers.size, dtype=np.int32)
        tops[2:] = deriv == -1

        if numbers[1] > numbers[0]:
            for i, no in enumerate(tops):
                if no == 0:
                    tops[i] = 1
                else:
                    break
        else:
            tops[0] = 1

        if numbers[-2] < numbers[-1]:
            tops[-1] = 1

        return max([len(x) for x in str(tops)[1:-1].replace(' ','').split('1')])+2

