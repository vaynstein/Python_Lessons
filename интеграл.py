#import math
from math import *

def func (x):
    #return (1-x**2)**(1/2)
    #return 1/(1+x**2)
    #return x**2
    return (sin(x))**2



def integral(f, a, b, dx=1e-5):
    x=a
    S=0
    while x<=b:
       S += f(x)*dx
       x += dx
    return S


print('S=',  integral(lambda x: (sin(x))**2/2, 0, pi))


