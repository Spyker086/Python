
message = ["в",'5','часов','17','минут','температура','воздуха','была','+5','градусов']

i = 0
while i < len(message):
    tp_it = False
    if message[i].isnumeric():
        message[i] = f"{int(message[i]):02}"
        tp_it = True
    elif message[i][0] in ['+'] and message[i][1:3].isnumeric():
        message[i] = f"{message[i][0]}{int(message[i][1:3]):02}"
        tp_it = True

    if tp_it:
        message.insert(i, '"')
        message.insert(i + 2, '"')
        i = i + 3
    else:
        i = i + 1

print(message)

i = 0
total = ''
while i < len(message):
    if message[i] == '\"':
        total = total + (message[i] + message[i + 1] + message[i + 2] + ' ')
        i = i + 3
    else:
        total = total + message[i] + ' '
        i = i + 1
print(total)