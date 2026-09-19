from functools import reduce
arr = [1,2,3,4,5,6,7]
result=reduce(lambda a,b:a+b,arr)
print(result)
