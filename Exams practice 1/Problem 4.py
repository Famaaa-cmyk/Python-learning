file = open('Exam prac\parrot.txt', 'r')

parrots = file.readlines()

print(parrots)

print('-------------------')

newlist = []
for par in parrots:
    data = par.split(',')
    newlist.append(data)

print(newlist)