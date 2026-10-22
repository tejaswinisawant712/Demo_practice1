class Student:  # Define class
    def __init__(self, marks):  # Constructor
        self.__marks = marks  # Private variable

    def set_marks(self, marks):  # Method to update marks
        self.__marks = marks  # Update private data

    def display(self):  # Method to display marks
        print("Marks:", self.__marks)  # Print marks

s = Student(80)  # Create object
s.display()  # Display marks

s.set_marks(95)  # Change marks
s.display()  # Display updated marks
