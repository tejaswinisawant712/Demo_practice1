balance=5000
withdraw=2000

if withdraw<=balance:
    balance = balance-withdraw
    print("New balance:",balance)

else:
    print("Insufficient balance")    