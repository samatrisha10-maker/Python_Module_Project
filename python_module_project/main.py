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

print("Current Date and Time:", get_current_time())

print("JSON:", convert_to_json({"name": "Python", "level": "Beginner"}))

print("Random Number:", generate_random_num())

print("Current Directory:", get_current_directory())

print("Numbers Found:", find_numbers("I scored 85 in Python and 90 in SQL"))

print("Item Count:", count_items(["apple", "banana", "apple", "orange", "banana"]))

print("Combined Lists:", combine_lists([1, 2, 3], [4, 5, 6]))

print("Square Root:", calculate_sqrt_root(25))

print("Mean:", calculate_mean([10, 20, 30, 40, 50]))

print("Path Exists:", check_path_exists("main.py"))