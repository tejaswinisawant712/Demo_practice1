def print12(n):
    if n==0 or n==1:
        return 1

    return n* print12(n-1) 

print(print12(6))       