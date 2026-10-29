class Student:  # Create class
    college = "ABC College"

    @staticmethod  # Define static method
    def show():  # Create method
        print("Welcome to college")
        print("Python Programming")

    @staticmethod
    def add(a, b):  # Addition method
        print("Addition =", a + b)

Student.show()  # Call show method
Student.add(10, 20)  # Call add method
print(Student.college)  # Display college name