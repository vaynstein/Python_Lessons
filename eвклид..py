inp1=int(input('a='))
inp2=int(input('b='))

def nod(a,b):    
    while a!=0 and b!=0:
        if a>b: a=a%b
        else:   b=b%a            
    return a+b

print(nod(inp1, inp2))

