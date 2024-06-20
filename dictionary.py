sample_dict1: dict[str, float] = {'x': 1.41, 'y': 3.14, 'z': 1.73}
sample_dict2: dict[str, float] = {'y': 3.14, 'z': 1.73, 'x': 1.41}
print(sample_dict1)
print(sample_dict2)
print(f"{sample_dict1} == {sample_dict2} returns {sample_dict1 == sample_dict2}.")
print(sample_dict1['x'])
print(sample_dict1['z'])

try:
    print(sample_dict1['a'])
except KeyError as em:
    print("If we do sample_dict1['a'], we have the follwing message:")
    print(em)

sample_dict1['a'] = 2.71
print(sample_dict1)
print(sample_dict1['a'])
sample_dict1['x'] = 2.23
print(sample_dict1)
