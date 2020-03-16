def get_key(item):
    return item[1]


sec = []
for i in range(int(input())):
    sec.append(list(map(int, input().split())))
sec.sort(key=get_key)
k = 0
dots = ""
while len(sec) > 0:
    start = sec.pop(0)
    left = start[0]
    dot = right = start[1]
    while len(sec) > 0 and right >= sec[0][0]:
        if sec[0][1] <= right:
            dot = right = sec[0][1]
            left = sec[0][0]
        sec.pop(0)
    dots += " "+str(dot)
    k += 1
print(str(k)+"\n"+dots.strip())



