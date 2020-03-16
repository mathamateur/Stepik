import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt'.strip())
while r.text[0] != 'W':
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+r.text.strip())
    print(r.text)
print(r.text)