import unittest

from datetime_util import get_current_time
from json_util import convert_to_json
from random_util import generate_random_num
from os_util import get_current_directory
from re_util import find_numbers
from collections_util import count_items
from itertools_util import combine_lists
from math_util import calculate_sqrt_root
from statistics_util import calculate_mean
from pathlib_util import check_path_exists


class TestModules(unittest.TestCase):

    def test_datetime(self):
        result = get_current_time()
        self.assertIsNotNone(result)

    def test_json(self):
        result = convert_to_json({"name": "Python"})
        self.assertIsNotNone(result)

    def test_random(self):
        result = generate_random_num()
        self.assertIsNotNone(result)

    def test_os(self):
        result = get_current_directory()
        self.assertIsNotNone(result)

    def test_regex(self):
        result = find_numbers("I have 25 apples")
        self.assertEqual(result, ["25"])

    def test_collections(self):
        result = count_items(["apple", "apple", "banana"])
        self.assertEqual(result["apple"], 2)

    def test_itertools(self):
        result = combine_lists([1, 2], [3, 4])
        self.assertEqual(result, [1, 2, 3, 4])

    def test_math(self):
        result = calculate_sqrt_root(25)
        self.assertEqual(result, 5)

    def test_statistics(self):
        result = calculate_mean([10, 20, 30])
        self.assertEqual(result, 20)

    def test_pathlib(self):
        result = check_path_exists("main.py")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()