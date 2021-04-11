import os

path = '/home/rustam/Рабочий стол/Python/sultanov_rustam_dz7/task_4-5/some_data'
size_dict = {100: 0, 1000: 0, 10000: 0, 100000: 0}

for file in os.listdir(path):
    file_path = os.path.join(path, file)
    sz = os.stat(file_path).st_size
    if sz < 100:
        size_dict[100] += 1
    elif sz < 1000:
        size_dict[1000] += 1
    elif sz < 10000:
        size_dict[10000] += 1
    elif sz < 100000:
        size_dict[100000] += 1

print(size_dict)