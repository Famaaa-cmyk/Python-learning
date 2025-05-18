file = open('Exams practice 3/images.txt')
print(file.read())
lst = []
for line in file.readlines():
    line = line.strip()
    lst.append(line.split(' '))
print(lst)