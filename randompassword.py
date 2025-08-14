import random

#letter,number,symbols


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#input user
username = input("Enter your username: ")
lettersamount = int(input("Enter the amount of letters: "))
numbersamount = int(input("Enter the amount of numbers: "))
symbolsamount = int(input("Enter the amount of symbols: "))

#random

letterslst = []
numberslst =[]
symbolslst =[]

for i in range (0,lettersamount):
    letter =letters[random.randint(0,len(letters)-1)]
    letterslst.append(letter)

for i in range (0,numbersamount):
    number  =letters[random.randint(0,len(numbers)-1)]
    numberslst.append(number)

for i in range (0,symbolsamount):
    symbol =symbols[random.randint(0,len(symbols)-1)]
    symbolslst.append(symbol)

password = letterslst + numberslst + symbolslst
random.shuffle(password)
passwordstr ="".join(password)

print(f"your password is {passwordstr}")

#save
with open("saved_passwords.txt", "a") as file:
    file.write(f"Username: {username} | Password: {passwordstr}\n")

