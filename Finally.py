try:
    num = 0
    result = 10 / num  # Divide 10 by num
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")  # Handle the exception

finally:
    print("Finally block executed")  # Always executes