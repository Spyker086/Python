
list_elem = []
sum_number = 0
sum_number_17 = 0

for elem in range(0, 1000):
    if elem % 2 != 0:
        elem = elem ** 3
        list_elem.append(elem)
print(list_elem)

for number in list_elem:
    sum_figure = 0
    sum_figure_17 = 0
    while number > 0:
        sum_figure = sum_figure + number % 10
        sum_figure_17 = sum_figure_17 + (number + 17) % 10
        if sum_figure % 7 == 0:
            sum_number = sum_number + number
        if sum_figure_17 % 7 == 0:
            sum_number_17 = sum_number_17 + (number + 17)
        number = number // 10

print(sum_number)
print(sum_number_17)