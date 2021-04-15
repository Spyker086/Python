

def type_logger(func):
    def log(*args, **kwargs):
        list_type = []
        for arg in args:
            list_type.append(f'{arg}:{type(arg)}')
        for key, value in kwargs.items():
            list_type.append(f'key= {key}, value= {value}:{type(value)}')
        print([i ** 3 for i in args])
        print(f'{func.__name__},{list_type}')
        # return func
    return log


@type_logger
def calc_cube(*args, **kwargs):
    return print(args)


calc_cube(5, 8, 3, num='sssqqq')