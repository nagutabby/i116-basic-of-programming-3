
def partition(pivot: int, l: list[int]) -> tuple[list[int], list[int]]:
    pair: tuple[list[int], list[int]] = ([], [])
    while len(l) > 0:
        e: int = l[0]
        l = l[1:]
        first_list: list[int] = pair[0]
        second_list: list[int] = pair[1]

        if e < pivot:
            pair = ([e] + first_list, second_list)
        else:
            pair = (first_list, [e] + second_list)
    return pair

def quick_sort(l: list[int]) -> list[int]:
    if len(l) <= 1:
        return l
    else:
        pair: tuple[list[int], list[int]] = partition(l[0], l[1:])
        return quick_sort(pair[0]) + [l[0]] + quick_sort(pair[1])

l: list[int] = [4, 7, 5, 1, 0, 3, 6, 2]
print(f'Input: {l}')
print(f'Output: {quick_sort(l)}')
