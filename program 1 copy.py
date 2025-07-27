
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','m','l','n','o','p','q','r','s','t','u','v','w','x','y','z'
            'a','b','c','d','e','f','g','h','i','j','k','m','l','n','o','p','q','r','s','t','u','v','w','x','y','z'
            ]

def caesar(text,shiftamount,direction):
    finaltext=""
    if direction == "decode":
        shiftamount = shiftamount * -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            newposition = position + shiftamount
            finaltext += alphabet[newposition]
        else:
            finaltext += char
    print(f"{direction}ed message is {finaltext}")

isend = False
while not isend:
    direction = input("Chose encode or decode:")
    message = input ("Enter the message:")
    shift = int(input("Enter the  shift number:"))

    caesar (text=message, shiftamount = shift ,direction=direction )
    restart = input("Do you wanna continue : yes or no :")
    if restart == "no":
        isend = True
        print("Thanks for using my program")
 
