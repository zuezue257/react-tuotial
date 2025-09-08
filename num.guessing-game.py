
import random
mynum = random.randrange(51)
mynum = 4

chance = 5

print('My number is between 1 and 50')
print('You have', chance , 'chance')
usernum = int ( input("Guess number"))

while usernum != mynum and chance > 1 :

    print ('Sorry ! wrong answer')

    if usernum > mynum:
        print('Your number greater')
    elif usernum < mynum:
        print (' Your number smaller')

    chance -= 1
    usernum = int (input('Guess the number'))

if usernum == mynum:
    print('Congratulations ! You got it')

else:
    print('Gmae over')
    print (' My num is',mynum)
    

