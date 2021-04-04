
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    s = sum(1 for line in open('nginx_logs.txt', 'r', encoding='utf-8'))
    result_list = []
    for l in range(s):
        line = f.readline().split()
        result_list.append((line[0], line[5], line[6]))
    print(result_list)





