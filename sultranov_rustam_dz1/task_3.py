percent = int(input("Введите проценты: "))

per_ed = percent % 10

if percent < 10 or per_ed == 1:
    print(str(percent) + " процент")
elif 2 <= per_ed < 5 and percent > 20:
    print(str(percent) + " процента")
elif 2 <= per_ed < 5 or 11 <= percent < 20:
    print(str(percent) + " процентов")