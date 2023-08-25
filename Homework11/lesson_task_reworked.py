import random
import json

file_path = 'data.json'


def json_file_random_reader(path, key: str):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        random_value = random.choice(data[key])
        return random_value


class NameGenerator:
    def __init__(self, number):
        self.number = number
        self.counter = 0

    def generate_names(self):
        while self.counter < self.number:
            name = ''.join(json_file_random_reader(file_path, "2") for _ in range(random.randint(1, 10)))
            self.counter += 1
            yield name + str(self.counter)


name_gen = NameGenerator(4)
for item in name_gen.generate_names():
    print(item)
