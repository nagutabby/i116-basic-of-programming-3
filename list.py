sample_list: list[int] = [0, 1, 2, 3, 4]
print(sample_list)
print(sample_list[0])
print(sample_list[1])
print(sample_list[-1])
print(sample_list[-2])

sample_list[2] = 10
print(sample_list) # sample_list[2] = 10 changes sample_;list.

try:
    sample_list[5]
except IndexError as em:
    print('If we try to do sample_list[5], the following message is written:')
    print(em)

print(sample_list[1:4])
print(sample_list[2:1])
print(sample_list[1:]) # deleting the top element
print(sample_list[:-1]) # deleting the bottom element
print(sample_list[100:])
print(sample_list[:-100])
print(sample_list) # sample_list[1:4] ... do not change sample_list.
print(sample_list[-100:100]) # seems strange but returns the list stored in sample_list
print(sample_list + sample_list)
print(sample_list) # + does not change sample_list.
print([-1] + sample_list)
print(sample_list + [5])
