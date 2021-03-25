

def thesaurus(args):
    args = args.split()
    symb_list_uniq = []
    name_list_total = []
    symb_uniq = set([i[0] for i in args])
    for symb in symb_uniq:
        symb_list_uniq.append(symb)
        symb_list_uniq.sort()
    for symb in symb_list_uniq:
        name_list = [i for i in args if i[0] == symb]
        name_list_total.append(name_list)
    dict_total = dict(zip(symb_list_uniq, name_list_total))
    # print(symb_list_uniq)
    # print(name_list_total)
    print(dict_total)


names = input("Ввпедите имена через пробел: ")
thesaurus(names)
