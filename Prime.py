num=int(input("Enter no:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1

if count ==2:
    print("Prime no")

else:
    print("Not prime no")            