file = open(r'Exam Practice Friday\wrong.products.csv')
lines = file.readlines()
s = 'store;product_name;price\n'
for line in lines[1:]:
    p,n,store = line.strip().split(',')
    s = s + str(store) + ';' + str(n) + ';' + str(p) + '\n'

s = s.strip()
newfile = open('products.csv', 'w')
newfile.write(s)