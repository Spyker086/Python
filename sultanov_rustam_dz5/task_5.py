
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def uniq_list(list_num):
    uniq_l = []
    for n in list_num:
        if list_num.count(n) == 1:
            uniq_l.append(n)
    return uniq_l

print(uniq_list(src))