a = 5
b = 10


def decorator(func):
    def wrapper(*args):
        print("Before the old code")
        func(*args)
        print("After the old code")

    return wrapper


@decorator
def simple_function(a, b):
    print(f'Var a = {a} and var b = {b}')


simple_function(a, b)

name = 'Alex'


def make_compliment(func):
    def wrapper(a):
        print(f'You are good {a}')
        func(a)
        print(f'Bye {a}!')

    return wrapper


@make_compliment
def ask_name(my_name):
    print(f'Hello {my_name}!!!')


ask_name(name)
