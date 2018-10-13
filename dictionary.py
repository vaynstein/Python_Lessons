f = open('input.txt', mode='r', encoding='utf-8')

#for line in f:
#    print(line, end='')
text = f.read()

D = {}

for litera in text:
    litera = litera.upper()
    D[litera] = D.get(litera, 0) + 1
    #print(litera)

for litera in sorted(D.keys(), key=lambda k:D[k]):
    print(litera, D[litera])

f.close()
