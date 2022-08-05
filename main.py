import random


number = input('guess a number betwen 1 and 15: ')

# generating a random number betwen 1 and 15
rando = random.randrange(1,15)


# checking if the input is the same number as the random number
if number == rando: 
    print('Yeah you got the right number! The number was: ' + str(number))
else:
    print('Sorry bro. The right number was: ' + str(rando))

