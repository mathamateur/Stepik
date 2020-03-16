import sys
sys.stdin = open(r'C:\Users\Aleksandr\PycharmProjects\stepik1\input','r')
p = {}


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

print(p)

for i in range(int(input())):
    a, b = input().split()
    if p.keys().__contains__(a) and p.keys().__contains__(b):
        if a == b or bfs(b, a):
            print('Yes')
        else:
            print('No')
    else:
        print('No')