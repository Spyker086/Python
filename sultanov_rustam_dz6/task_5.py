import sys


def users_hobby(file_names, file_hobby, file_total):
    total_dict = {}

    with open(file_names, 'r', encoding='utf-8') as n, open(file_hobby, 'r', encoding='utf-8') as h:
        names = n.readline().strip()
        hobby = h.readline().strip().split(',')
        while names:
            names = ''.join(names.split(','))
            total_dict.update({names: hobby})
            names = n.readline().strip()
            hobby = h.readline().strip().split(',')
    with open(file_total, 'w', encoding='utf-8') as t:
        t.write(str(total_dict))
    # return total_dict


if __name__ == "__main__":
    file_names = sys.argv[1]
    file_hobby = sys.argv[2]
    file_total = sys.argv[3]
    results = users_hobby(file_names, file_hobby, file_total)
    exit(0)