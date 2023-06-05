﻿from collections import defaultdict

def combine_dicts(*args):
    result = defaultdict(int)
    for dictionary in args:
        for key, value in dictionary.items():
            result[key] += value
    return dict(result)

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2, dict_3))