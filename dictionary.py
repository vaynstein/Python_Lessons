f = open('input.txt', mode='r', encoding='utf-8')
text = f.read()
f.close()

D = {}

for litera in text:
    litera = litera.upper()
    D[litera] = D.get(litera, 0) + 1


for litera in sorted(D.keys(), key=lambda k:D[k], reverse=True):
    print(litera, D[litera])

