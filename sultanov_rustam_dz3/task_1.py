

def num_tranclate(key):
    return tranc.setdefault(key, "!!!Неверно задано значение!!!")


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
