import random

database = {333333333 :{"name" : "Mg Mg" , "password":"123456" , "amount":5000},
            
            44444444 :{"name": "Kyaw Kyaw", "password": "111111" , "amount": 80000}}



def home():
    print("    Welcome to my bank.   ")
    print("    --------------------- ")
    return input("1. Create account\n2. Account login\n3. Option :")
     
def menu():
    
    return input("1. Check Balance \n2. Deposit \n3. Withdraw \n4. Exit \n5. Options :" )

def createacc():
    name = input("Name:")
    password = input ("Password")
    confirmpassword = input ( "Confirm Password" )
    while password != confirmpassword:
        print("Your password did not same")
        password = input ("Password")
    confirmpassword = input ( "Confirm Password" )

    accountno = random.randrange(100000000,1000000000)

    while accountno in database:
        accountno = random.randrange(100000000,1000000000)

    database[accountno] ={}
    database[accountno]["name"] = name
    database[accountno]["password"] = password
    database[accountno]["amount"] = 0

    menu()
status = home()
while status != "q" :
 status = home()
 if status == "1":
        createacc()
     


 elif status == "2":
   useracc = int(input("Enter your account number :"))
   if useracc not in database:
        print("Your account is not registered :")
    
        useroption = input ("1. Create an account \n2.exit \n3 Options ")
        if input == "1" :
            createacc()
        else:
            exit ()

 else:
  password = input("Enter your password :")
  while database[useracc]["password"] != password:
   print("Wrong Password!")
   password = input("Enter your password :" )

  else:
    print("Invalid Option")
    print("#################")

  status = home()



        

