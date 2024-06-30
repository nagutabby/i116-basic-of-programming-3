sample_dict1: dict[str, float] = {'x':1.41, 'y':3.14, 'z':1.73}
sample_dict2: dict[str, float] = {'y':3.14, 'z':1.73, 'x':1.41}
print(sample_dict1)
print(sample_dict2)
print(f'{sample_dict1} == {sample_dict2} returns {sample_dict1 == sample_dict2}.')

x:int  = 0
for k in sample_dict1:
    x = x + 1
    if k == 'z':
        break
print('x = ', x)

x = 0
for k in sample_dict2:
    x = x + 1
    if k == 'z':
        break
print('x = ', x)
