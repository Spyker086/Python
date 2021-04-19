import re


p = sum(1 for line in open('/home/rustam/Рабочий стол/Python/sultanov_rustam_dz6/nginx_logs.txt', 'r'))

with open('/home/rustam/Рабочий стол/Python/sultanov_rustam_dz6/nginx_logs.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    reguest_list = []
    k = 0
    while line:
        ip_pattern = re.compile(r'\d{,3}.\d{,3}.\d{,3}.\d{,3}')
        ip_total = re.match(ip_pattern, line)
        reguest_list.append(ip_total.group(0))
        # print(ip_total)

        data_pattern = re.compile(r'\d{,2}/\w+/\d{4}:\d{2}:\d{2}:\d{2}\s[+]0000')
        data_total = re.findall(data_pattern, line)
        reguest_list.append(data_total[0])
        # print(data_total[0])

        type_pattern = re.compile(r'[A-Z]{3}')
        type_total = re.findall(type_pattern, line)
        reguest_list.append(type_total[0])

        http_pattern = re.compile(r'/[a-z]+/[a-z_0-9]+')
        http_total = re.findall(http_pattern, line)
        reguest_list.append(http_total[0])

        code_pattern = re.compile(r'\d+\s\d+')
        code_total = re.findall(code_pattern, line)
        code = code_total[0].split()[0]
        size = code_total[0].split()[1]
        reguest_list.append(code)
        reguest_list.append(size)

        reguest_tuple = tuple(reguest_list)
        line = f.readline()
        print(reguest_tuple)
        reguest_list = []
        k += 1

    if k == p:
        print('\n!!!Все строки обработаны!!!')
    else:
        print('\n!!!СБОЙ СУММЫ СТРОК!!!')

    f.close()