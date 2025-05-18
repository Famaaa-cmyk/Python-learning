file = open('Exams practice 3/cat.txt')

lst = []
for line in file.readlines():
    line = line.strip()
    lst.append(line.split(' '))
print(lst)