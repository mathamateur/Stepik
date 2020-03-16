n = int(input())
k = 0
s = ""
for i in range(n + 1):
    for j in range(1, i + 1):
        s += (str(i) + " ")
        k += 1
        if k == n:
            print(s)
            break
