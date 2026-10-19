class Student:
    def __init__(self):  # Constructor
        self.name = "Rahul"
        self.age = 20

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s = Student()  # Create object
s.display()    # Call method