class Bank:  # Define class
    def __init__(self, balance):  # Constructor
        self.__balance = balance  # Private variable

    def deposit(self, amount):  # Method to deposit money
        self.__balance += amount  # Add amount to balance

    def display(self):  # Method to display balance
        print("Balance:", self.__balance)  # Print balance

b = Bank(1000)  # Create object
b.display()  # Display balance
b.deposit(500)  # Deposit money
b.display()  # Display updated balance
