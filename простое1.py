#n=int(input('n='))

def prime(n):
    if n==2:
        return True
    elif n%2==0:
        return False
    else:
        i = 3
        m = int((n) ** (1 / 2))
        while i<=m:
            if n%i==0:
                return False                
            i+=2
    return True
    
def ferma(n):
    return 2**(n-1)%n==1


#if prime(n):
#   print('простое',n)
#else:
#   print('составное',n)

for k in range(2, 10000):
    if prime(k):
        print(k)

 
