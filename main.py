# todo Logical Operator  (and, or , not )

# user_Name = input("Enter your username: ")
# good = int(input("How many good? "))

# # Enter Evil Bob and Elise

# if user_Name == "bob" or user_Name == "Elise" : 
#   if good < 4 : 
#    print("Dont Come In")
#    exit()  
# elif user_Name == "Bob" and good > 4 :
#   print("Hello Not evil Bob your welcome here")

# else :
#   print("Please come in") 


print("Welcome to Arc Coffee Shop \n")

# Create a log-in
# Username && Password 

user_Name = input("Enter your username: ")
user_Pass = input("Enter your password: ")

# List of Evil Customer 
# Yohan, Gilbert, Bernard 

if user_Name == "Yohan" or user_Name == "Gilbert" or user_Name == "Bernard" :
  print(f"{user_Name}, Your not welcome here!!!!")
