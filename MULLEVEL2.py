class Grandfather:
    def M1(self):  # Define M1 method
        print("Grandfather method")

class Parent(Grandfather):  # Inherit Grandfather
    def M2(self):  # Define M2 method
        print("Parent method")

class Child(Parent):  # Inherit Parent
    def M3(self):  # Define M3 method
        print("Child method")

c = Child()  # Create Child object
c.M1()  # Call Grandfather method
c.M2()  # Call Parent method
c.M3()  # Call Child method