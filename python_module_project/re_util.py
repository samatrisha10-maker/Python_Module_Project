import re

def find_numbers(text):
    result = re.findall(r"\d+",text)
    return result
print(find_numbers("I scored 85 in Python and 90 in SQL"))