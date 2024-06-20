def merge(first_list: list[int], second_list: list[int]) -> list[int]:
    if len(first_list) == 0:
        return second_list
    elif len(second_list) == 0:
        return first_list
    else:
        if first_list[0] < second_list[0]:
            return [first_list[0]] + merge(first_list[1:], second_list)
        else:
            return [second_list[0]] + merge(first_list, second_list[1:])

def merge_sort(l: list[int]) -> list[int]:
    if len(l) <= 1:
        return l
    else:
        first_list: list[int] = []
        second_list: list[int] = []
        flag: bool = True
        while len(l) > 0:
            if flag:
                first_list = [l[0]] + first_list
            else:
                second_list = [l[0]] + second_list
            l = l[1:]
            flag = not flag
        return merge(merge_sort(first_list), merge_sort(second_list))

l: list[int] = [4,7,5,1,0,3,6,2]
print('Input: ', l)
print('Output: ', merge_sort(l))
