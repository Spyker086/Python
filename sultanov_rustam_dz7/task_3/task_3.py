import os
import shutil


if not os.path.isdir('templates'):
    os.mkdir('templates')

path = '/home/rustam/Рабочий стол/Python/sultanov_rustam_dz7/task_3/my_project'
path_copy = '/home/rustam/Рабочий стол/Python/sultanov_rustam_dz7/task_3/templates'

for root, dirs, files in os.walk(path):
    # print(root, dirs, files)
    for file in files:
        if file.split('.')[-1] == 'html':
            # print(os.path.split(root))
            folder = os.path.split(root)[-1]
            os.chdir('templates')
            if not os.path.isdir(folder):
                os.mkdir(folder)
            os.chdir(root)
            shutil.copy(file, os.path.join(path_copy, folder))
            os.chdir('/home/rustam/Рабочий стол/Python/sultanov_rustam_dz7/task_3')


