def percent_of_product_with_args(percent, *args):
    product = 1
    for number in args:
        product = product * number
    return product / 100 * percent


print(percent_of_product_with_args(10, 100, 235, 578))


# kwargs

def hello_with_greeting_and_kwargs(greeting, **kwargs):
    if 'name' in kwargs:
        print('{}! Nice to meet you, {}'.format(greeting, kwargs['name']))
    else:
        print('{}! What is your name?'.format(greeting))


hello_with_greeting_and_kwargs('Hello', gender='make', age=24, name='Jack')
