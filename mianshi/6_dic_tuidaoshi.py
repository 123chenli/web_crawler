"""
d = {key: value for (key, value) in iterable}
"""
mcase = {'a': 10, 'b': 3}
print(mcase.items())
mcase_frequency = {v: k for k, v in mcase.items()}
print(mcase_frequency)