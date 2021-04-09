
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

name_klass = ((n,k) for n,k in zip(tutors, klasses))
print(type(name_klass))
print(list(name_klass))

def name_klass_none(name, klass):
    delta = len(name) - len(klass)
    if delta > 0:
        klass.extend([None for i in range(delta)])
    for n, k in zip(name, klass):
        yield n, k

name_klass2 = name_klass_none(tutors, klasses)
print(type(name_klass2))
print(list(name_klass2))



