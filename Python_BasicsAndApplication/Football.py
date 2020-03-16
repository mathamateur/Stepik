n = int(input())
d = {}
a = []
for i in range(n):
    s = input().strip().split(';')
    a.extend(s)
for i in range(0,len(a),2):
    key = a[i]
    if key not in d:
        d[key] = [0, 0, 0, 0, 0]
for i in range(1,len(a)-2,4):
    d[a[i-1]][0] += 1
    d[a[i+1]][0] += 1
    if a[i] > a[i+2]:
        d[a[i-1]][1] += 1
        d[a[i+1]][3] += 1
        d[a[i-1]][4] += 3
    elif a[i] == a[i+2]:
        d[a[i-1]][2] += 1
        d[a[i-1]][4] += 1
        d[a[i+1]][2] += 1
        d[a[i+1]][4] += 1
    else:
        d[a[i-1]][3] += 1
        d[a[i+1]][1] += 1
        d[a[i+1]][4] += 3
for key,value in d.items():
    value = str(value[0]) + " " + str(value[1]) + " " + str(value[2]) + " " + str(value[3]) + " " + str(value[4])
    print(str(key) + ":" + value)