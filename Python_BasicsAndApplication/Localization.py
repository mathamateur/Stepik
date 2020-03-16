x = y = 0
for i in range(int(input())):
    k = input()
    if  k[0] == "в":
        x += int(k.split()[1])
    elif k[0] == "з":
        x -= int(k.split()[1])
    elif k[0] == "с":
        y += int(k.split()[1])
    else:
        y -= int(k.split()[1])
print(x,y)