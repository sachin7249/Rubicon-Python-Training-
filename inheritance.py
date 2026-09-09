class animal:
    def eat(self):
        print("animal is eating")


class Dog(animal):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()
d.bark()
