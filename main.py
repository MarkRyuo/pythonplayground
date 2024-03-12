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
# Lily, Gilbert, Bernard 

if user_Name == "Lily" or user_Name == "Gilbert" or user_Name == "Bernard" : # using Logical Operator
    user_Identity = input("Are you Evil? (Yes/No) : ")
    if user_Identity == "Yes" or user_Identity == "No" :
      user_Clarify = int(input("How many good ways do you have?: "))
      if user_Clarify < 3 :
       print(f"{user_Name}, You're not welcome here!!!!")
       exit()
      else :
        print(f"{user_Name}, Sorry for mistake your good your welcome here")
else :
  print(f"Hello {user_Name}, welcome the arc coffee shop!\n \n")

# List of coffee's 

# I use Array here g
list = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha"] 

print(f"This is the list of Coffee's {list}")

