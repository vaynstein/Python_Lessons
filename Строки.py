A=[]
while True:
    a=input('>')
    if a=='': break        
    A.append(a)

A.sort(key=int)

#for c in range(len(A)-1, -1,-1):
#    print(A[c])
    

for c in A: print(c)    
    
        
