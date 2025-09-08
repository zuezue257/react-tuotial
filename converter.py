
print("-----------Conveter Program-----------")

print("1.lenght")

print ("2.weight")

print("3.temperature")

userinput = input ("Chose your option:")

if userinput == "1" :
    print("1.km to mile")
    print("2. mile to kilometer")
    userinput = input ("Chose your option :")
 
    if userinput == "1":
         fromvalue = int(input("Enter kilometer :"))
         tovalue = fromvalue / 1.6
         print (fromvalue, "km" , tovalue,"mile")

         
    
    elif userinput == "2":
         fromvalue = int (input("Enter mile :"))
         tovalue = fromvalue * 1.6
         print (fromvalue, "miles" , tovalue,"km")
    else :
         print("Invalid Choice")


elif userinput == "2":
     print("1.kg to lg")
     print("2. pound to kg ")
     userinput = input ("Chose your option :")

     if userinput =="1":
         fromvalue = int (input("Enter kilogram :"))
         tovalue = fromvalue * 2.2
         print (fromvalue, "kilogram" , tovalue,"pound")

     elif userinput == "2" :
          fromvalue = int (input("Enter Pound :"))
          tovalue = fromvalue * 1.6
          print (fromvalue, "pound" , tovalue,"kilogram")

     else:
          print("Invalid choice")

elif userinput == "3":
      print("1.Celsius to Fahrenheight")
      print("2. Fahrenheight to Celsius ")
      userinput = input ("Chose your option :")


      if userinput == "1" :
           fromvalue = int (input("Enter celsuius :"))
           tovalue = fromvalue * 9/5 + 32
           print (fromvalue, "celsuius" , tovalue,"fahrenheight")

      elif userinput == "2" :
            fromvalue = int (input("Enter fahrenheight :"))
            tovalue = (fromvalue - 32 ) * 5/9
            print (fromvalue, "fahrenheight" , tovalue,"celsius")
      else:
           print("Invalid choicce")

else:
    print ("Invalid choice")