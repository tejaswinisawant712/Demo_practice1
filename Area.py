
print("1. Triangle")
print("2. Circle")
print("3. Square")
print("4. Rectangle")

ch = int(input("Enter your choice: "))

if ch == 1:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area =", 0.5 * b * h)

elif ch == 2:
    r = float(input("Enter radius: "))
    print("Area =", 3.14 * r * r)

elif ch == 3:
    s = float(input("Enter side: "))
    print("Area =", s * s)

elif ch == 4:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print("Area =", l * b)

else:
    print("Invalid choice")
