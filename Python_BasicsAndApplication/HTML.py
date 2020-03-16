import requests
import re


with open(r'C:\Users\Aleksandr\PycharmProjects\stepik1\input','r') as f, open('output.txt','w') as fw:
    res = requests.get(f.readline().strip())
    [print(i) for i in sorted(set(re.findall(r'<a.*href=[\'"](?:\w*://)?(\w[\w\d.\-]*).*[\'"]', res.text)))]