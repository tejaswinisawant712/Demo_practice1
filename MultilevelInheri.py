class Students:  # Parent class
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

class Marks(Students):  # Child class
    def __init__(self, name, roll_no, m1, m2, m3):
        super().__init__(name, roll_no)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def display(self):
        total = self.m1 + self.m2 + self.m3
        avg = total / 3

        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Total Marks:", total)
        print("Average Marks:", avg)

# Take input from user
name = input("Enter name: ")
roll_no = int(input("Enter roll number: "))
m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))

# Create object
s = Marks(name, roll_no, m1, m2, m3)

# Display details
s.display()