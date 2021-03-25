
list_kub = []
sum_number = 0
sum_number_17 = 0

for elem in range(0, 1000):
    if elem % 2 != 0:
        elem = elem ** 3
        list_kub.append(elem)
# print(list_kub)

for number in list_kub:
    sum_figure = 0
    sum_figure_17 = 0
    while number > 0:
        sum_figure = sum_figure + number % 10
        sum_figure_17 = sum_figure_17 + (number+17) % 10
        # print(sum_figure)
        if sum_figure // 7 == 0:
            sum_number = sum_number + number
        number = number // 10
        if sum_figure_17 // 7 == 0:
            sum_number_17 = sum_number_17 + (number +17)
print(sum_number)
print(sum_number_17)


# print(list_kub)

# p = 4321
# p = p % 10
# print(p)


# a = 0
# a_deg = 0 # "а" в степени 3
# a_deg_17 = 0 # "а" в степени 3 + 17
# sum = 0 # итого
# sum_17 =0 #  итого +17
#
# while a < 1000:
#     if a % 2 == 0:
#         a_deg = a ** 3
#         a_deg_17 = a ** 3 + 17
#         k = a_deg // 100000000
#         i = a_deg // 10000000 % 10
#         h = a_deg // 1000000 % 10
#         g = a_deg // 100000 % 10
#         f = a_deg // 10000 % 10
#         e = a_deg // 1000 % 10
#         d = a_deg // 100 % 10
#         c = a_deg // 10 % 10
#         b = a_deg % 10
#         k_17 = a_deg_17 // 100000000
#         i_17 = a_deg_17 // 10000000 % 10
#         h_17 = a_deg_17 // 1000000 % 10
#         g_17 = a_deg_17 // 100000 % 10
#         f_17 = a_deg_17 // 10000 % 10
#         e_17 = a_deg_17 // 1000 % 10
#         d_17 = a_deg_17 // 100 % 10
#         c_17 = a_deg_17 // 10 % 10
#         b_17 = a_deg_17 % 10
#         if (k + i + h + g + f + e + d + c + b) % 7 == 0:
#             sum = sum + a_deg
#         if (k_17 + i_17 + h_17 + g_17 + f_17 + e_17 + d_17 + c_17 + b_17) % 7 == 0:
#             sum_17 = sum_17 + a_deg_17
#     a = a + 1
# print(sum)
# print(sum_17)