class Employee:  # Parent class
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):  # Child class
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):  # Redefine method
        print("Full-time Salary:", self.salary)

class PartTimeEmployee(Employee):  # Child class
    def __init__(self, rate, hours):
        self.rate = rate
        self.hours = hours

    def calculate_salary(self):  # Redefine method
        print("Part-time Salary:", self.rate * self.hours)

f = FullTimeEmployee(30000)  # Create object
p = PartTimeEmployee(200, 5)  # Create object

f.calculate_salary()  # Call full-time method
p.calculate_salary()  # Call part-time method