def substrings(s, a, b):
    if a in b and a in s:
        return "Impossible"
    elif a not in s:
        return 0
    else:
        return substrings(s.replace(a, b), a, b) + 1


a = set()
s = input()
t = input()
for i in range(len(s)):
    if s.find(t,i) != -1:
        a.add(s.find(t,i))
print(len(a))