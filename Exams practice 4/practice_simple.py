# basic score for a student to enter university is 80 
# if student is a Hafiz he can get extra 10 marks 
# write a programe that will print if you qualified for exams or not

marks = float(input('enter your marks'))
hafiz = input('Are you a Hafiz?')
if hafiz == 'yes':
    marks = marks +10
if marks >= 80:
    print(f'you are qualified for university with marks {marks}' )
else:
    print('sorry next time')
    
    

    



