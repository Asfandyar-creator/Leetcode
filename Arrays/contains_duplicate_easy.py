class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return f'a {self.color} car with {self.mileage} miles'

blue_car = Car('blue', 20)
print(blue_car)

class Parent:
    speaks = ['English']

class Child(Parent):
    def __init___(self):
        super().__init__()
        self.speaks = ['Spanish']


class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def __str__(self):
        return f'{self.name} is a {self.age} year old {self.breed}'
    def __repr__(self):
        