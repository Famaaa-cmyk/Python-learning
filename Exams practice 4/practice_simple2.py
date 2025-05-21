# for shop we have database 
# if user enter the product name and if that is present in data base it should print the product is available 
# else it should print sorry product is not available

databse = ['apple','orange','mango','strawberry','shampoo','soup','chicken','lamb']
p = input('enter to check if product is available:')

if p in databse:
    print(f'{p} is available')
else:
    print(f'{p} is not availible')


