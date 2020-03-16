s1=input()
k = 1
x = s1[0]
s2 = ""
for i in range(1,len(s1)):
    if s1[i-1] == s1[i]:
        k += 1
    else:
        s2 += x + str(k)
        x = s1[i]
        k = 1
print(s2 + x + str(k))