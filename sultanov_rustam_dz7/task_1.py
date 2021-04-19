import os

dir_name = ['my_project', 'settings', 'mainapp', 'adminapp', 'authapp']
os.chdir('task_3')
if not os.path.isdir(dir_name[0]):
    os.mkdir(dir_name[0])
os.chdir('my_project')
for i in dir_name[1:]:
    if not os.path.isdir(i):
        os.mkdir(i)
