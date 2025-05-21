#Hoemwork 2
#Temperature checker 
#Write a program that checks the temperature.
#If it is below 0, then print it is 'freezing'
#if it is between 0 and 40, print normal temperature 
#If it is over 40, warn the user that it is extremely hot. 

Temperature = input('Enter a temperature: ')
Temperature = int(Temperature)
if Temperature <= 0:
    print('It is freezing')
elif Temperature <=40:
        print('It is normal temperature')
elif Temperature >=40:
     print('It is extremelu hot')
else:
      print('Enter a valid temperature')