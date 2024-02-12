import re
def find_pattern(pattern,data):
    result=re.findall(rf"{pattern}", data)
    return result

pat="chait[r, u]"
email_data="chaitra <chaitrasradha@gmail.com>, anu <anusha@gmail.com>, chaitu03 <chaitra11@gmail.com>, chintu <chintu@gmail.com>"
res=find_pattern(pat,email_data)
print(res)

pat1="[A-Za-z0-9_]+@[A-Za-z0-9]+\.[A-Za-z0-9]+"
email_data="chaitra <chaitrasradha@gmail.com>, anu <anusha@gmail.com>, chaitu03 <chaitra11@gmail.com>, chintu <chintu@gmail.com>"
res1=find_pattern(pat1,email_data)
print(res1)

pat2="chait[u, z]+[0-9]+"
email_data="chaitra <chaitrasradha@gmail.com>, anu <anusha@gmail.com>, chaitu03 <chaitra11@gmail.com>, chintu <chintu@gmail.com>"
res2=find_pattern(pat2,email_data)
print(res2)

pat3="\w+@\w+\.\w+"
email_data="chaitra <chaitrasradha@gmail.com>, anu <anusha@gmail.com>, chaitu03 <chaitra11@gmail.com>, chintu <chintu@gmail.com>"
res3=find_pattern(pat3,email_data)
print(res3)
