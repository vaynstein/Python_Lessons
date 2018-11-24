N = 1000
A = [True]*N

i = 2
m = N**(1/2)
while i < m:
    while not A[i]:
        i += 1
    k = 2*i
    while k < N:
        A[k] = False
        k +=i
    i += 1

for k in range(2, N):
    if A[k]:
        print(k)


