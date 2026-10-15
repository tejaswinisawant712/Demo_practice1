a = [2, 4, 6, 8, 10]
prefix = [0] * len(a)

prefix[0] = a[0]

for i in range(1, len(a)):
    prefix[i] = prefix[i - 1] + a[i]

print("Prefix Sum:", prefix)