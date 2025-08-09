#password save program


def savepassword(service,username,password):
    """Save the password information to a file."""
    with open("passwords.txt","a")as file:
        file.write(f"{service}|{username}|{password}/n")
    print("password save successfully")
def main():
    print("===Password Saver===")
    while True:
       service = input ("Enter the service/website name:")
       username = input ("Enter your user name:")
       password =input("Enter your password:")
       savepassword(service,username,password) 
       choice = input("add anothr password? ").lower()
       if choice != 'y':
          print ("Exiting program")
          break
main()
