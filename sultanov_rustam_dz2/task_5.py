
prices = [2, 3.15, 74.1, 15, 8.54, 12.75, 4, 17.4]

i = 0
prices_str = ''
for item in prices:
    prices_str = prices_str + f"{int(item // 1)} руб {round((item - int(item)) * 100):02} коп, "
    i = i + 1
print("1:")
print(prices_str)

i = 0
prices_str = ''
for item in sorted(prices):
    prices_str = prices_str + f"{int(item // 1)} руб {round((item - int(item)) * 100):02} коп, "
    i = i + 1
print ("2:")
print(prices)
print(prices_str)

prices.sort(reverse = True)
i = 0
prices_str = ''
for item in prices:
    prices_str = prices_str + f"{int(item // 1)} руб {round((item - int(item)) * 100):02} коп, "
    i = i + 1
print ("3:")
print(prices_str)

i = 0
prices_str = ''
for item in sorted(prices)[-1:-6:-1]:
    prices_str = prices_str + f"{int(item // 1)} руб {round((item - int(item)) * 100):02} коп, "
    i = i + 1
print ("4:")
print(prices_str)
