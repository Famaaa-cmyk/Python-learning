people_dict = {
    "Emma": 28,
    "Liam": 35,
    "Olivia": 42,
    "Noah": 31,
    "Ava": 39,
    "Ethan": 26,
    "Sophia": 33,
    "Mason": 45,
    "Isabella": 29,
    "William": 37,
    "Mia": 59,
    "James": 30,
    "Charlotte": 36,
    "Benjamin": 27,
    "Amelia": 34,
    "Lucas": 38,
    "Harper": 32,
    "Alexander": 43,
    "Evelyn": 25,
    "Daniel": 40
}

for people in people_dict:
    print(f'{people} has the age {people_dict[people]}.')


print(f'Mia is especially invited beacuse she is {people_dict["Mia"]}')