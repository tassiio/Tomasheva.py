list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def find_func(lst_first, lst_sec):
    for x in lst_first:
        for y in lst_sec:
            yield x, y, x * y


for item in find_func(list_1, list_2):
    if item[2] == to_find:
        print(item[0], '*', item[1], '=', to_find)
        # break
