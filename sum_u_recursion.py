def print12():
    if n==0:
        return 0

    return n + print12(n-1) 

print(print12(7))       