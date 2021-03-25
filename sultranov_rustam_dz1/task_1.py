
duration = int(input("Введите ко-во секунд: "))
# print("Секунды = " + str(duration))

if duration < 60:
    print("sec:" + str(duration % 60))
if duration < 3600:
    print("min:" + str(duration // 60) + " sec:" + str(duration % 60))
elif 3600 <= duration < 86400:
    print("h:" + str(duration // 3600) + " min:" + str(duration % 3600 // 60) + " sec:" + str(duration % 60))
elif duration >= 86400:
    print("days:" + str(duration // 86400) + " h:" + str(duration % 86400 // 3600) + " min:" + str(
        duration % 3600 // 60) + " sec:" + str(duration % 60))
