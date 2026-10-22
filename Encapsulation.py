class Student:  # Define class
    def __init__(self):  # Constructor
        self.__marks = 90  # Private variable

    def display(self):  # Define method
        print(self.__marks)  # Print marks

s = Student()  # Create object
s.display()  # Call method
