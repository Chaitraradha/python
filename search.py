import re
email_data="chaitra <chaitrasradha@gmail.com>, anu <anu@gmail.com>, chitra <chitra@gmail.com>"
res=re.search("ch", email_data)
print(res)
email_data="chaitra <chaitrasradha@gmail.com>, anu <anu@gmail.com>, chitra <chitra@gmail.com>"
res=re.findall("ch", email_data)
print(res)

