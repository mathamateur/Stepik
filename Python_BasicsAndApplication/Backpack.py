n, w = map(int, input().split())
items = []
price = 0.0
for i in range(n):
    items.append(list(map(int, input().split())))
items.sort(key=lambda x: x[0]/x[1], reverse=True)
while w > 0 and len(items) > 0:
    item = items.pop(0)
    if item[1] <= w:
        price += item[0]
    else:
        price += item[0]*w/item[1]
    w -= item[1]
print('%.3f' % price)