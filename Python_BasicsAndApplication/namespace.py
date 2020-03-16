children = {'global': []}
var = {'global': []}


def contains(k,x):
    a = []
    a.extend(var[k])
    for i in a:
        if i == x:
            return True
    return False


def val(d,x):
    for k,v in d.items():
        for j in v:
            if x == j:
                return k


def add(k,v):
    a = [v]
    a.extend(var[k])
    var[k] = a


def create(k,v):
    a = [v]
    a.extend(children[k])
    children[k] = a
    children[v] = []
    var[v] = []


def get(k,v):
    if k == 'global' and not contains(k,v):
        return 'None'
    if contains(k,v):
        return k
    return get(val(children,k),v)


n = int(input())

for i in range(n):
    a,b,c = input().split()
    if a == 'add':
        add(b,c)
    elif a == 'create':
        create(c,b)
    else:
        print(get(b,c))