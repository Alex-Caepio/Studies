from functools import wraps


def check_if_first_arg_is(value):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                print(f'First argument has to be {value}')
            return func(*args, **kwargs)

        return wrapper

    return inner_dec


@check_if_first_arg_is('blue')
def print_colors(*colors):
    print(colors)


@check_if_first_arg_is(7)
def multiply_7(a, b):
    return a * b


print_colors('red', 'blue', 'green')
print(multiply_7(2, 5))


def enforce(*types):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = []
            for a, t in zip(args, types):
                new_args.append(t(a))
            return func(*new_args, **kwargs)

        return wrapper

    return inner_dec


@enforce(str, int)
def print_text_n_times(text, n):
    for _ in range(1, n):
        print(text)


@enforce(int, int)
def divide(a, b):
    return a / b


print_text_n_times('Hello', '5')
print(divide('10', '5'))
