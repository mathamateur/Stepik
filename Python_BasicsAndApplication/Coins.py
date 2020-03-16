# Для монет любых номиналов. Сложность O(n)
k = 0
n = int(input())
coins = list(map(int, input().split()))
for i in range(len(coins) - 1, -1, -1):
    k += n // coins[i]
    n -= n // coins[i] * coins[i]
print(k)

# Для монет номиналом[1, 5, 10, 25]. Сложность O(1)
# a25 = n//25
# a10 = (n - a25*25)//10
# a5 = (n - a25*25 - a10*10)//5
# a1 = n - a25*25 - a10*10 - a5*5
# k = a25 + a10 + a5 +a1
# print(k)