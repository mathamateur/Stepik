def primes():
    x = 2
    while True:
        flag = True
        for i in range(2,int(x**0.5)+1):
            if x % i == 0:
                flag = False
                break
        if flag:
            print(x)
        x += 1
