# Parent class
class Animal:
    def eat(self):
        print("Animal is eating")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Create an object
d = Dog()

d.eat()   # Inherited method
d.bark()  # Child class method
