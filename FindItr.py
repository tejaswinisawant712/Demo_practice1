import re
text="python is easy python is simple,python"
result=re.finditer("python",text)
for match in result:
    print(match.group(),match.start(),match.end())