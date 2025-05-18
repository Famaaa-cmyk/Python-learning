def give_marks(marks):

    marks = float(marks)
    if marks < 50:
        print('Fail')
    elif marks >= 50 and marks < 80:
        print('Grade B')
    elif marks >=80 and marks <90:
        print('Grade A')
    elif marks >=90 and marks < 100:
        print('A+')
    else:
        
        print('invalid keep values between 0 to 100')

