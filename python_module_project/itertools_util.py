import itertools

def combine_lists(list1 , list2):
    result = itertools.chain(list1 , list2)
    return list(result)
print(combine_lists([1,2,3],[4,5,6,]))