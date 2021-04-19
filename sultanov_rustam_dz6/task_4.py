
total_dict = {}

with open('csv/users.csv', 'r', encoding='utf-8') as n, open('csv/hobby.csv', 'r', encoding='utf-8') as h:
    names = n.readline().strip()
    hobby = h.readline().strip().split(',')
    while names:
        names = ''.join(names.split(','))
        total_dict.update({names: hobby})
        names = n.readline().strip()
        hobby = h.readline().strip().split(',')

print(total_dict)
with open('total.csv', 'w', encoding='utf-8') as t:
    t.write(str(total_dict))