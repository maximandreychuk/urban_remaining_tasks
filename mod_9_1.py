def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        res = func(int_list)
        results[func.__name__] = res
    return results


def plus_one(lst):
    return [number + 1 for number in lst]

def sum_lst(lst):
    return sum(lst)

def min_value(lst):
    return min(lst)

def sort_lst(lst):
    return sorted(lst)


integers = [1,3,-42,9,2]
print(apply_all_func(integers, plus_one, min_value, sum_lst, sort_lst))

