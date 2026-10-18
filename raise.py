try:
    age = -5  # Store age
    if age < 0:
        raise ValueError("Age cannot be negative")    #manually generate an exception.
    print("Age =", age)  # Display age

except ValueError as e:
    print("Error:", e)  # Handle the exception

finally:
    print("Finally block executed")  # Always executes