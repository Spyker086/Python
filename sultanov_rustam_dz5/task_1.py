
def num_odd(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

odd_to_15 = num_odd(15)
print(next(odd_to_15))
print(next(odd_to_15))