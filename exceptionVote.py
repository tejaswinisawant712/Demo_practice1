try:
    age = int(input("Enter your age: "))  # Get age from user

    if age < 0:
        raise ValueError("Age cannot be negative")

    elif age >= 18:
        print("Eligible for voting")
    else:
        print("Not eligible for voting")

except ValueError as e:
    print("Error:", e)  # Handle exception

finally:
    print("Finally block executed")  # Always executes