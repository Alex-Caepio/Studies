import time


class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self, weight):
        time.sleep(1)
        print(f"load: {weight} max load: {self.max_load}")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


new_car = Car('bmw', 2, 2345, 200)
new_car.move()
new_car.stop()
print(new_car.brand)
print(new_car.color)
print(new_car.age)
new_car.birthday()
print(new_car.age)

new_truck = Truck('Volvo', 3, 1234, 1000)
new_truck.move()
new_truck.stop()
print(new_truck.brand)
print(new_truck.color)
print(new_truck.age)
new_truck.birthday()
print(new_truck.age)
new_truck.load(1000)
