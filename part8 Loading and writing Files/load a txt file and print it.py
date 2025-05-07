file = open(r'C:\Users\Bruker\OneDrive\Skrivebord\Python learning\part9 Error handling\fruits.txt')
print('file is ',file)
data = file.read()
for each in data.split('\n'):
    a,b = each.split(' ')
    b = int(b)
    b = b* 1.1
    print(a,b)
