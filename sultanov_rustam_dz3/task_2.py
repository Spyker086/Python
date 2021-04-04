

def num_tranclate(key):
    if key.istitle():
        result = tranc.setdefault(key.lower(), "!!!Неверно задано значение!!!")
        return result.title()
    else:
        result = tranc.setdefault((key), "!!!Неверно задано значение!!!")
        return result


tranc = {
"one":"один",
"two":"два",
"three":"три",
"four":"четыре",
"five":"пять",
"six":"шесть",
"seven":"семть",
"eigth":"восемь",
"nine":"девять",
"ten":"десять"}

key = input("Введине число на английском от 1 до 10: ")
print(num_tranclate(key))
