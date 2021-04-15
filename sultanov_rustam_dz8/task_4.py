from functools import wraps

def val_checker(chek):
    def checker(func):
        @wraps(func)
        def wrapper(*args):
            x = args[0]
            if chek(x):
                return func(x)
            else:
                raise ValueError(f'Error value {x}')
        return wrapper
    return checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return print(x ** 3)

calc_cube(-5)

