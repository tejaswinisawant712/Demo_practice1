def print12(n):
    if n>0:
        print12(n-1)
        print(n)

    else:
        print("Execution completed")

print12(12)            