sample_tuple: tuple[int, str, float] = (0, 'zero', 0.0)
print(sample_tuple)
print(f'{()} is the empty tuple.')
print(f"{('zero',)} is the tuple that only consists of 'zero'.")
print("('zero') is not a tuple but a string, the same as 'zero'.")
print(f"('zero') == 'zero' returns {('zero') == 'zero'}.")
print(f"('zero',) == 'zero' returns {('zero',) == 'zero'}.")
print(sample_tuple[0])
print(sample_tuple[1])
print(sample_tuple[-1])
print(sample_tuple[-2])

try:
    # Unsupported target for indexed assignment ("tuple[int, str, float]")
    sample_tuple[2] = 1.41421356
except TypeError as e:
    print('If we try to do sample_tuple[2] = 1.41421356, the following message is written:')
    print(e)

try:
    # Tuple index out of range
    sample_tuple[3]
except IndexError as e:
    print('If we try to do sample_tuple[3], the following message is written:')
    print(e)

sample_tuple = (sample_tuple[0], sample_tuple[1], 1.41421356)
print(sample_tuple)
