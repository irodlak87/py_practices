import pytest
import numpy as np

from exercises.base_exercises import find_substring_idx, find_perfect_squares, find_deepest_pit


class TestBasics(object):

    @pytest.mark.parametrize('string,substring,expected_idx',
                             [('alma', 'lm', 1),
                              ('aaalaaallalma', 'lm', 10),
                              ('frghih', 'frghi', 0)
                              ])
    def test_find_substring_idx(self, string, substring, expected_idx):
        assert find_substring_idx(string, substring) == expected_idx

    @pytest.mark.parametrize('start,end,expected_result',
                             [(0, 10, np.array([0, 1, 4, 9])),
                              (4, 16, np.array([4, 9, 16])),
                              ])
    def test_find_perfect_squares(self, start, end, expected_result):
        assert np.all(np.equal(find_perfect_squares(start, end), expected_result))

    @pytest.mark.parametrize('numbers,expected_result',
                             [
                              ([0,1,2,3,2,4,3,2,5], 4),
                              ([0, 1, 0, 3, 8, 9, 7, 8, 0], 3),
                              ([0, -1, -2, -3, 8, 7, 8, 7, 6], 5),
                              ([0, -1, -2, -3, 8, 9, 10, 7, 6], 7),
                              ])
    def test_find_deepest_pit(self, numbers, expected_result):
        assert find_deepest_pit(numbers) == expected_result
