a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

if a!=0:    
    d=b**2-4*a*c
    if d>0:
        x1=(-b+d**(1/2))/(2*a)
        x2=(-b-d**(1/2))/(2*a)
        print('x1=',x1)
        print('x2=',x2)
    elif d==0:
        x=-b/(2*a)
        print('x=',x)        
    else:
        print('решений нет')
        
elif b!=0:
     x=-c/b
     print('x=',x)     
elif c==0:
     print('x=любое число')
else:
     print('решений нет')
        

        
        
        
     
