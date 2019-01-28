from time import time

start = time()

def prime(n):
    i = 3
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        while i <= int((n) ** (1 / 2)):
            if n % i == 0:
                return False
            i += 2
    return True


def expmod(x, n, m):
    res = 1
    x %= m
    while n > 0:
        if n % 2 == 0:
            n //= 2
            x = x*x % m
        else:
            n -= 1
            res = res*x % m
    return res



def ferma(n):
    return 2 ** (n - 1) % n == 1

def ferma2(n):
    return expmod(2, n-1, n) == 1

def ferma3(n):
    return pow(2, n-1, n) == 1


for k in range(2, 500000):
    if ferma3(k) and not prime(k):
        print(k)

print('Время выполнения: {} с'.format( round(time()-start, 3) ))
