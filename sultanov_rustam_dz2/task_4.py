

positions = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

i = 0
b = 0
name = ''
while i < len(positions):
    b = positions[i][::-1].find(' ')
    name = positions[i][len(positions[i]) - b:len(positions[i]) + b:]
    print(f"Привет, {name.capitalize()}!")
    i = i + 1

