# load data
# save it as nested list
# ask user to enter the product (keep on asking using while loop)
# if product is present in nested list save it in cart
# if programe ends give total bill

file = open('Exams practice 3/product.txt')

lst = []

for line in file.readlines():
    line = line.strip()
    line = line.split(' ')
    lst.append(line)



names = []
prices = []
categry = []
for line in lst:
    names.append(line[0])
    prices.append(line[1])
    categry.append(line[2])
print(names)
print(prices)

cart = []

loop = True
while loop == True:

    name = input(f'Enter the product name: ') 
    if name in names:
        cart.append(name)
    if name == 'quit':
        break

print('you have chosen',cart)
tot = 0
for n in names:
    position = names.index(n)
    tot += float(prices[position])
print('total bill is ',tot)