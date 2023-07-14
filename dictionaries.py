car_prices = {'opel': 5000, 'toyota': 7000, 'bmw': 10000}
print(car_prices)
print(car_prices['toyota'])
car_prices['mazda'] = 4000
print(car_prices)
del car_prices['toyota']
print(car_prices)

person = {
    'first name': 'Jack',
    'last name': 'Brown',
    'age': 43,
    'hobbies': ['football', 'singing', 'photo'],
    'children': {'son': 'Michael', 'daughter': 'Pamela'}
}

print(person['age'])
print(person['hobbies'][2])

michael_data = person['children']['son']
print(michael_data)

person['children']['second_son'] = 'Bobby'
print(person)

person['hobbies'][0] = 'basketball'
print(person['hobbies'])

print(person.keys())
print(person.values())

if 43 in person.values():
    print(True)

print(person.items())
