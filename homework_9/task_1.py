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


new_car = Auto('bmw', 2, 2345)
new_car.birthday()
new_car.move()
new_car.stop()
new_car.color = 'red'
print(new_car.brand)
print(new_car.color)
print(new_car.age)
