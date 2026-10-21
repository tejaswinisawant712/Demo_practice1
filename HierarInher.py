class Parent:
    def show(self):
        print("This is parent class")

class Child1(Parent):
    def display1(self):
        print("This is child 1")

class Child2(Parent):
    def display2(self):
        print("This is child 2")

obj1 = Child1()
obj1.show()
obj1.display1()

obj2 = Child2()
obj2.show()
obj2.display2()