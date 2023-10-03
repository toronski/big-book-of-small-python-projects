import datetime, random

def getBirthday(numBdays):
    birthdays = []

    for i in range(numBdays):
        date = datetime.date(2001, 1, 1)
        birthday = date + datetime.timedelta(random.randint(0, 364))
        birthdays.append(birthday)
    
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA
            
def main():
    print('''\n\nDid you know that in a group of 70 people
propability that 2 people
will have birthdays on the same day
is 99,9%? And in a group of 20, it's 50%!
          
          This program is going to prove that to you.\n\n''')
    
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    print('Enter the number of birthdays to generate:')

    while True:
        response = input('> ')
        if response.isdecimal() and (0 <= int(response) <= 100):
            break

    numBdays = int(response)
    birthdays = getBirthday(numBdays)
    
    print('Here are ', numBdays, ' generated birthdays: \n')

    for i, birthday in enumerate(birthdays):
        if i != 0:
           print(',', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')
        
    match = getMatch(birthdays)

    if match != 0:
        print("\nWe have some duplicate here.")
    else:
        print("\nWe don't have any duplicate here.")

    print('\nTime to test on a bigger scale!')
    print('\nLet\'s run 100 000 simulations.\n')

    repetitions = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(i, 'operations were performed...')
        birthdays = getBirthday(numBdays)
        if getMatch(birthdays) != None:
            repetitions += 1

    repPercent = round((repetitions/100_000) * 100, 2)

    print('''\nAfter 100 000 simulations,
the percentage of repetitions was as much as {}% !
\nAmazing, isn't it?'''.format(repPercent))


main()