import requests
import json

d = {}
with open(r'C:\Users\Aleksandr\PycharmProjects\stepik1\dataset_24476_4.txt','r') as f:
    artists = f.readlines()
client_id = '3b6a71060e19c5936d7a'
client_secret = 'a8e11c1ffc501dc467abebcb619ca755'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)
token = j["token"]

headers = {"X-Xapp-Token" : token}
params = {"id": ""}
api_url = "https://api.artsy.net/api/artists/"
for artist in artists:
    res = requests.get(api_url+artist.strip(), headers=headers)
    res.encoding = 'utf-8'
    j = json.loads(res.text)
    if not d.__contains__(j["birthday"]):
        d[j["birthday"]] = [j["sortable_name"]]
    else:
        d[j["birthday"]].append(j["sortable_name"])
with open(r'output.txt','w',encoding='UTF-8') as fw:
    [(print(k),fw.write(v+'\n')) for k in sorted(d.keys()) for v in sorted(d[k])]

