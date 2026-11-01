class Student:  # Parent class
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

class Sports:  # Parent class
    def __init__(self, sport):
        self.sport = sport

class Result(Student, Sports):  # Child class
    def __init__(self, name, roll_no, sport):
        Student.__init__(self, name, roll_no)
        Sports.__init__(self, sport)

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Sport:", self.sport)

# Take input from user
name = input("Enter name: ")
roll_no = int(input("Enter roll number: "))
sport = input("Enter sport: ")

# Create object
r = Result(name, roll_no, sport)

# Display details
r.display()