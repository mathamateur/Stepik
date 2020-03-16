d = {}
ud = {}
s1 = input()
s2 = input()
s3New = ""
s4New = ""
for i in range(len(s1)):
    d[s1[i]] = s2[i]
    ud[s2[i]] = s1[i]
s3 = input()
s4 = input()
for i in range(len(s3)):
    s3New += str(d[s3[i]])
print(s3New)
for i in range(len(s4)):
    s4New += str(ud[s4[i]])
print(s4New)