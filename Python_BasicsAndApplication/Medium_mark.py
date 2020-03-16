d = {}
with open(r"C:\Users\Пользователь\Documents\input.txt",'r') as f:
    for line in f:
        s = line.strip().split(';')
        d[s[0]] = s[1:len(s)]
med = medAbs1 = medAbs2 = medAbs3 = 0
for key,value in d.items():
    med = (float(value[0])+float(value[1])+float(value[2]))/3
    medAbs1 += float(value[0])
    medAbs2 += float(value[1])
    medAbs3 += float(value[2])
    d[key] = str(med)
n = len(d)
with open(r"C:\Users\Пользователь\Documents\output.txt",'w') as ouf:
    for value in d.values():
        ouf.write(value + '\n')
    ouf.write(str(medAbs1/n) + " " + str(medAbs2/n) + " " + str(medAbs3/n))
