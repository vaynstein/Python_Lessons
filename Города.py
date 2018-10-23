r=open('base/country.csv',mode='r',encoding='cp1251')
D={}
for line in r:
    line=line.strip()
    R=line.split(';')
    country_id=R[0].strip('"')
    name=R[2].strip('"')
    D[country_id]=name
    print(country_id,name)

f=open('base/city.csv', mode='r',encoding='cp1251')
for line in f:
    #print(line,end='')
    line=line.strip()
    C = line.split(';')
    country_id = C[1].strip('"')
    region_id=C[2].strip('"')
    name=C[3].strip('"')
    print('Город {} находится в стране {} в регионе {}'.format(name,D[country_id],region_id))


