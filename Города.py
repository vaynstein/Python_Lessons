f=open('base/city.csv', mode='r',encoding='cp1251')
for line in f:
    #print(line,end='')
    line=line.strip()
    C = line.split(';')
    country_id = C[1].strip('"')
    region_id=C[2].strip('"')
    name=C[3].strip('"')
    print('Город {} находится в стране {} в регионе {}'.format(name,country_id,region_id))



