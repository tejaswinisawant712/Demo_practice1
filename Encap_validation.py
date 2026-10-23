
class Student:  # Define class
    def __init__(self, marks):  # Constructor
        self.__marks = marks  # Private variable

    def set_marks(self, marks):  # Method to update marks
        if marks >= 0 and marks <= 100:  # Check valid marks
            self.__marks = marks  # Update marks
        else:
            print("Invalid marks")  # Show error message

    def display(self):  # Method to display marks
        print("Marks:", self.__marks)  # Print marks

s = Student(80)  # Create object
s.display()  # Display marks

s.set_marks(95)  # Set valid marks
s.display()  # Display updated marks

s.set_marks(120)  # Set invalid marks
