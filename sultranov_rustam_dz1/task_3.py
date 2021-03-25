percent = int(input("Введите проценты: "))

per_ed = percent % 10

if 10 < percent <= 20:
    print(str(percent) + " процентов")
elif per_ed == 1:
    print(str(percent) + " процент")
elif 2 <= per_ed < 5:
    print(str(percent) + " процента")
elif per_ed > 4 or per_ed == 0:
    print(str(percent) + " процентов")