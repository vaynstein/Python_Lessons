r=open('base/country.csv',mode='r',encoding='cp1251')
D={}
for line in r:
    line=line.strip()
    R=line.split(';')
    country_id=R[0].strip('"')
    name=R[2].strip('"')
    D[country_id]=name
    #print(country_id,name)


k=open('base/region.csv',mode='r',encoding='cp1251' )
M={}
for line in k:
    line = line.strip()
    N=line.split(';')
    country_id = N[1].strip('"')
    region_id = N[0].strip('"')
    name1 = N[3].strip('"')
    M[region_id] = name1




f=open('base/city.csv', mode='r',encoding='cp1251')
for line in f:
    #print(line,end='')
    line=line.strip()
    C = line.split(';')
    #city_id=C[0].strip('"')
    country_id = C[1].strip('"')
    region_id=C[2].strip('"')
    name = C[3].strip('"')
    #D[city_id]=name2
    print('Город {} находится в стране {} в регионе {}'.format(name, D[country_id],M[ region_id] ))
