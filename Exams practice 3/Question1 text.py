file = open('Exams practice 3/cars.txt')
main_list = []
for line in file.readlines():
    line = line.strip()
    regnr, brand, start_date = line.split(' ')
    main_list.append([regnr,brand,start_date])
print(main_list)