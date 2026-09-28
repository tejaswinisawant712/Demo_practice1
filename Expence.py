expenses = []                                      # Creates empty list for expenses

n = int(input("How many expenses do you want to add? "))  # Gets number of expenses

for i in range(n):                                 # Repeats for each expense
    name = input("Enter expense name: ")            # Gets expense name
    amount = float(input("Enter amount: "))         # Gets expense amount
    expenses.append([name, amount])                 # Stores name and amount

total = 0                                           # Starts total amount from zero

print("\n--- Expense Details ---")                  # Prints heading

for expense in expenses:                            # Goes through each expense
    print(expense[0], ":", expense[1])              # Displays expense details
    total += expense[1]                             # Adds amount to total

print("-----------------------")                     # Prints separator
print("Total Expense =", total)                     # Displays total expense