# todo Logical Operator  (and, or , not )

user_Name = input("Enter your username: ")
good = int(input("How many good? "))

# Enter Evil Bob and Elise

if user_Name == "Bob" or user_Name == "Elise" : 
  if good < 4 : 
   print("Dont Come In")
   exit()  
elif user_Name == "Bob" and good > 4 :
  print("Hello Not evil Bob your welcome here")
else :
  print("Please come in") 