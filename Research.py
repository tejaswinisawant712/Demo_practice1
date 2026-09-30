import re
text= "i am python trainer because python is easy "
result= re.search("python",text)

if result:
    print("found")

else:
    print("not found")    