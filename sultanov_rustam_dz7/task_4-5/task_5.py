import os
import json

path = '/home/rustam/Рабочий стол/Python/sultanov_rustam_dz7/task_4-5/some_data'
size_dict = {100: 0, 1000: 0, 10000: 0, 100000: 0}
count_100 = 0
count_1000 = 0
count_10000 = 0
count_100000 = 0
list_ext_100 = []
list_ext_1000 = []
list_ext_10000 = []
list_ext_100000 = []

for file in os.listdir(path):
    file_path = os.path.join(path, file)
    sz = os.stat(file_path).st_size
    if sz < 100:
        count_100 += 1
        if file.split('.')[-1] not in list_ext_100:
            list_ext_100.append(file.split('.')[-1])
    elif sz < 1000:
        count_1000 += 1
        if file.split('.')[-1] not in list_ext_1000:
            list_ext_1000.append(file.split('.')[-1])
    elif sz < 10000:
        count_10000 += 1
        if file.split('.')[-1] not in list_ext_10000:
            list_ext_10000.append(file.split('.')[-1])
    elif sz < 100000:
        count_100000 += 1
        if file.split('.')[-1] not in list_ext_100000:
            list_ext_100000.append(file.split('.')[-1])

size_dict[100] = (count_100, list_ext_100)
size_dict[1000] = (count_1000, list_ext_1000)
size_dict[10000] = (count_10000, list_ext_10000)
size_dict[100000] = (count_100000, list_ext_100000)

path_dz = os.getcwd().split('/')[-1]
file_path_dz = os.path.join(os.getcwd(), f'{path_dz}_summary.json')
with open(file_path_dz, 'w', encoding='utf-8') as t:
    json.dump(size_dict, t)
