
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    s = sum(1 for line in open('nginx_logs.txt', 'r', encoding='utf-8'))
    result_list_ip = []
    result_dict = {}

# Получаем список ip-адресов
    for l in range(s):
        line = f.readline().split()
        result_list_ip.append(line[0])

# Получаем список уникальных ip-адресов
uniq_ip_list = []
uniq_ip = set(i for i in result_list_ip)
for ip in uniq_ip:
    uniq_ip_list.append(ip)

# Получаем словарь IP : количество запросов
p = {i:result_list_ip.count(i) for i in uniq_ip_list}
max_requests = max(p.values())

# Определяем IP с максимальным значением запросов
def get_ip(p, max):
    for ip, v in p.items():
        if v == max:
            return ip

print(f'IP: {get_ip(p, max_requests)}, кол-во запросов: {max_requests}')

