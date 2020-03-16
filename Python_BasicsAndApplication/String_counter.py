a = []
with open(r"C:\Users\Пользователь\Documents\input.txt",'r') as f:
    for line in f:
        line = line.strip()
        s = line.lower().split()
        a.extend(s)
d = {}
for i in range(len(a)):
    d[a[i]] = 0
for i in range(len(a)):
    d[a[i]] += 1
valueMax = keyMax = 0
for key,value in d.items():
    if value >= valueMax:
        if value > valueMax:
            valueMax = value
            keyMax = key
        elif key < keyMax:
            valueMax = value
            keyMax = key
with open(r"C:\Users\Пользователь\Documents\output.txt",'w') as ouf:
    ouf.write(str(keyMax) + " " + str(valueMax))
