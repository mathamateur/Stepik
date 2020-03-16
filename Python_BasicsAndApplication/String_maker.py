with open(r"C:\Users\Пользователь\Documents\input.txt",'r') as inf:
    s = inf.readline()
size = len(s)-1
s1 = ""
s2 = ""
a = []
while size > -1:
    if (s[size] >= "0") and (s[size] <= "9"):
        s1 += s[size]
    else:
        s2 += s[size]*int(s1[::-1])
        s1 = ""
    size -= 1
print(s2[::-1])
with open(r"C:\Users\Пользователь\Documents\output.txt",'w') as ouf:
    ouf.write(s2[::-1])
