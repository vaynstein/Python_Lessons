print('gold=', (5**(1/2)+1)/2 )
a, b = 1, 1
while b<=100000000:
    print(a,b/a)
    a, b = b, a+b
   
