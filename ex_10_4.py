def prime(n):
    i = 3
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        m = int(n**(1 / 2))
        while i <= m:
            if n % i == 0:
                return False
            i += 2
    return True



def sumc(n):
    return sum(map(int, list(str(n))))

m = 100

for p in range(2, 10000000):
    if prime(p):
        n = (p**2 + 2)**2 - 9*(p**2 - 7)
        c = sumc(n)
        #print(p, n, c)
        if c < m:
            m = c
            pm = p
            nm = n

print()
print(pm, nm, m)

