#Question 4
#Les CSV fil og split linjene til en 2D - liste 
#Skriv så ny fil med ny kolonnerekkerfølge. 
#Les filen linje for linje 
#Split llinjer på ; og lag en 2D liste
#Skriv til ny fik med koloonerekkeføllge: VNr;Description;Cat.No,;Shelf;Price;Quantity

#Les csv filen 
file = open(r'Last_day practice\produkter.csv')
line = file.readlines()
s = ''
for line in line:
    c,v,shelf,p,d,q = line.strip().split(';')
    s = s + str(v)+';'+str(d)+';'+str(c)+';'+str(shelf)+';'+str(p)+';'+str(q)+ '\n'
s = s.strip()
newfile = open('correctproducts.csv','w')
newfile.write(s)
