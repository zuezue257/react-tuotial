#python password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

lettersamount =int(input("Enter the amount of letters:"))
numsamount = int(input("Enter the amount of numbers:"))
symbolsamount = int (input("Enter the amount of symbols:"))

letterslst = []
numberslst =[]
symbolslst =[]

for i in range (0,lettersamount):
    letter =letters[random.randint(0,len(letters)-1)]
    letterslst.append(letter)

for i in range (0,numsamount):
    number  =letters[random.randint(0,len(numbers)-1)]
    numberslst.append(number)

for i in range (0,symbolsamount):
    symbol =symbols[random.randint(0,len(symbols)-1)]
    symbolslst.append(symbol)

password = letterslst + numberslst + symbolslst

random.shuffle(password)
passwordstr ="".join(password)
print(f"your password is {passwordstr}")