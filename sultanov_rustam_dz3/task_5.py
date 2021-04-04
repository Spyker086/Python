from random import choice, sample


def get_jokes(quantity, repeats):
    jokes = []
    if repeats == "Да":
        for i in range(quantity):
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        print(jokes)
    else:
        zipped = zip(sample(nouns, quantity), sample(adverbs, quantity), sample(adjectives, quantity))
        for i in zipped:
            i = " ".join(i)
            jokes.append(i)
        print(jokes)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# p = list(zip(nouns, adverbs, adjectives))
# print(p)
rep = input("Разрешить повотры: ")
quan = int(input("Количество шуток: "))
get_jokes(quan, rep)