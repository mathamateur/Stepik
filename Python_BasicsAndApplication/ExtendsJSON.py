import json

p = {}
classes = []


def bfs(a, b):
    if p[a].__contains__(b):
        return 1
    elif len(p[a]) == 0:
        return 0
    else:
        for j in p[a]:
            return bfs(j, b) + 1


data = json.loads(input())
for i in range(len(data)):
    p[data[i]["name"]] = data[i]["parents"]
    classes.append(data[i]["name"])
classes = sorted(classes)
for i in range(len(classes)):
    k = 0
    for j in range(1,len(classes)):
        if i == j:
            continue
        k = bfs(classes[j],classes[i])
    print(classes[i]+' : '+str(k))
