N = 1000
A = [True]*(N+1)

for i in range(2, int(N**(1/2)+1)):
    k = 2*i
    while k <= N:
        A[k] = False
        k +=i

for k in range(2, N+1):
    if A[k]:
        print(k)


