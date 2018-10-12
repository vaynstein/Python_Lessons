#n=int(input('n='))

def prime(n):
    i=3    
    if n==2:
        return True
    elif n%2==0:
        return False
    else:
        while i<=int((n)**(1/2)):
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

for k in range(2, 100000):
    if ferma(k) and not prime(k):
        print(k)
   
 
