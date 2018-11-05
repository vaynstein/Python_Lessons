from time import time

t0 = time()

db = {1 : 0}


def f1(n):
    x=n
    i=0
    while x>1:
        if x%2==0:
            x //= 2
        else:
            x=3*x+1
        i += 1
    return i


def f2(n):
    x=n
    i=0
    while x>1:
        if x%2==0:
            x //= 2
        else:
            x=3*x+1
        i += 1
        if x in db:
            i += db[x]
            break
    db[n] = i
    return i


def f3(n):
    if n in db:
        return db[n]
    x = n
    if x % 2 == 0:
        x //= 2
    else:
        x = 3*x + 1
    res = f3(x) + 1
    db[n] = res
    return res




m = 0
n = 0

for k in range(1, 1_000_000):
    r = f3(k)
    if r > m:
        n = k
        m = r

print(n, m)


print('Time: {} c'.format(time() - t0))