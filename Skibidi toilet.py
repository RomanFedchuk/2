class Cat:

    height = 170
    gladness = 0

class SmallCat(Cat):
    height = 100
    gladness = 0


class BigCat(Cat):
    height = 250
    gladness = 0

nick = Cat()
ann = SmallCat()

print(nick.height)
print(nick.gladness)
print(ann.height)
print(ann.gladness)


class Dog:
    height = 200
    gladness = 90
    age = 10

class BigDog(Dog):
    age = 15
    gladness = 100
    height = 400

class SmallDog(Dog):
    height = 100
    gladness = 50
    age = 2

    def __init__(self):
        print(self.height)
        print(self.gladness)
        print(self.age)


ch = Dog()
