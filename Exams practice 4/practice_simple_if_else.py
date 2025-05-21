# if a person work 37.5 hours he will be paid 20 usd per hour
# if a person works more than 37.5 hours in a week he will be paid 25 usd per hour with every extra hour
# write a program that will give me total earning based on hours worked


hours_worked =float( input('enter the number of hours:') )


#Works 37,5 hours he will be paid = 20 dollars per hour 
#more than 37,5 in a week he will be paid = 25 dollar for every extra hour
#program should give total earining based on hours worked 

if hours_worked >= 37.5:
    standard_pay = 37.5 * 20
    extra_money = (hours_worked - 37.5) * 25
else:
    standard_pay = hours_worked * 20
    extra_money = 0 

total = standard_pay + extra_money
print(f'The standard earning is {standard_pay}, the extra money he got was {extra_money}, the total is {total}')

 
