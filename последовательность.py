def function(n):
    x = n
    i = 0
    while x>1:
        if x%2==0:
            x //= 2
        else:
            x=3*x+1
        i += 1
    return i

Max = 0
Nm = 0


for k in range(1,1000):
    res = function(k)
    if res > Max:
        Max = res
        Nm = k

print(Nm, Max)



#print( "{1} {0}".format( *max((function(k), k) for k in range(1, 1000))))