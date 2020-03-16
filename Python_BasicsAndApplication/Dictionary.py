n = int(input())
a = []
c = []
b = set()
for i in range(n):
    a.append(input().lower())
n = int(input())
for i in range(n):
    s = input().lower().split()
    c.extend(s)
for i in range(len(c)):
    if c[i] not in a:
        b.add(c[i])
for value in b:
    print(value)