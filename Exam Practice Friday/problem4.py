file = open(r'C:\Users\Bruker\OneDrive\Skrivebord\Python learning\Exam Practice Friday\wrong_order.csv')
lines = file.readlines()
s = ''
for line in lines:
    f,l,m = line.strip().split(';')
    s = s +  str(f)+';'+str(m)+';'+str(l)+ '\n'

s = s.strip()
newfile = open('reorder.csv','w')
newfile.write(s)
