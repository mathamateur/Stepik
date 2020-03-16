import requests
import re

with open(r"C:\Users\Aleksandr\PycharmProjects\stepik1\input",'r') as f:
    a = f.readline().strip()
    b = f.readline().strip()
res = requests.get(a)
url = re.findall(r'<a.*</a>', res.text)
flag = False
if len(url) != 0:
    for i in url:
        match = re.match(r'.*href=[\'"](.*)[\'"]', i)
        if match is not None:
                res = requests.get(match.group(1))
        if re.search(b,res.text):
            flag = True
            break
if flag:
    print("Yes")
else:
    print("No")