import sys
sys.stdin = open(r'C:\Users\Aleksandr\PycharmProjects\stepik1\input','r')
p = {}
e = []
ul = []


def bfs(a, b):
    for i in p[a]:
        if i == b:
            return True
    for j in p[a]:
        if (bfs(j, b)):
            return True


for i in range(int(input())):
    s = input().split(' : ')
    if len(s) == 2:
        p[s[0]] = s[1].split()
        for j in p[s[0]]:
            if not p.keys().__contains__(j):
                p[j] = []
    else:
        p[s[0]] = []


for i in range(int(input())):
    e += input().split()
    if p.keys().__contains__(e[-1]):
        for j in range(len(e)-1):
            if bfs(e[-1],e[j]) and not ul.__contains__(e[-1]):
                ul.append(e[-1])

for i in range(len(ul)):
    print(ul[i])