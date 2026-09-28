from collections import Counter

def count_items(items):
    result = Counter(items)
    return result
print(count_items(["apple","banana","orange","apple","orange","apple","banana","orange","banana"]))