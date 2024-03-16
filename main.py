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


# print("Welcome to Arc Coffee Shop \n")

# # Create a log-in
# # Username && Password 

# user_Name = input("Enter your username: ")
# user_Pass = input("Enter your password: ")

# # List of Evil Customer 
# # Lily, Gilbert, Bernard 

# if user_Name == "Lily" or user_Name == "Gilbert" or user_Name == "Bernard" : # using Logical Operator
#     user_Identity = input("Are you Evil? (Yes/No) : ")
#     if user_Identity == "Yes" or user_Identity == "No" :
#       user_Clarify = int(input("How many good ways do you have?: "))
#       if user_Clarify < 3 :
#        print(f"{user_Name}, You're not welcome here!!!!")
#        exit()
#       else :
#         print(f"{user_Name}, Sorry for mistake your good your welcome here")
# else :
#   print(f"Hello {user_Name}, welcome the arc coffee shop!\n \n")

# # List of coffee's 

# # I use Array here g
# list = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha"] 

# print(f"This is the list of Coffee's {list}\n") 

# choose = input("What Coffee you love?: ")
# quantity = int(input("How many?: "))

# # I use if statement and elif 

# if choose == "Espresso" :
#   print(f"Your order is {list[0]}")
#   price = 50 
#   total = price * quantity
#   print(f"The price of {list[0]} is {price} per 1 and you ordered {quantity}, the total is ₱{total}.00") 
# elif choose == "Cappuccino" :
#   print(f"Your order is {list[1]}")
#   price = 50 
#   total = price * quantity
#   print(f"The price of {list[1]} is {price} per 1 and you ordered {quantity}, the total is ₱{total}.00") 
# elif choose == "Latte" :
#   print(f"Your order is {list[2]}")
#   price = 50 
#   total = price * quantity
#   print(f"The price of {list[2]} is {price} per 1 and you ordered {quantity}, the total is ₱{total}.00")
# elif choose == "Americano" : 
#   print(f"Your order is {list[3]}")
#   price = 50 
#   total = price * quantity
#   print(f"The price of {list[3]} is {price} per 1 and you ordered {quantity}, the total is ₱{total}.00")
# elif choose == "Mocha" :
#   print(f"Your order is {list[4]}")
#   price = 50 
#   total = price * quantity
#   print(f"The price of {list[4]} is {price} per 1 and you ordered {quantity}, the total is ₱{total}.00")
# else :
#   print("null") 

# # Todo Need multiple Elif need ✅
# #Todo Need Upgrade here 
# # todo update add if add 
  
# addAnother = input("Add Coffee: ")
# list.append(addAnother) #add in last
# list.insert(3, addAnother) # add in index 3 the new add coffee 
 
# print(list)

atuple = ("Jhon Mark", 21 , "01/19/03") 

print(type(atuple)) 

aarray = ["Jhon Mark", 21 , "01/19/03"] 

print(type(aarray))
