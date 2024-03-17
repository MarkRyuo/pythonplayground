# todo all knowledge to Network Chunk 

user_Name = input("Enter your name: ")

list_of_ban = {
  "Sophia",
  "Liam",
  "Emma",
  "Noah",
  "Olivia",
}

if user_Name == "Sophia" or user_Name == "Liam" or user_Name == "Emma" or user_Name == "Noah" or user_Name == "Olivia":
  #ask him/her if he evil // using nested loop  
  user_Identity = input("Are you a Evil?(Yes/No): ") 
  if user_Identity == "Yes" :
    print(f"Hey {user_Name}, Your not welcome here")
  elif user_Identity == "No": 
    user_Check = int(input(f"How many good way you have now {user_Name}?: "))
    if user_Check > 5 :
      print(f"{user_Name} welcome to the Arc Mini Coffee shop ")
    else :
      print(f"{user_Name}, you're not welcome here")
else :
  print(f"Hello {user_Name}")

user_Age = int(input("What is your age: "))

# Condition if age is less than or equal to 10 : too young to drink coffee
if user_Age <= 10 : 
  print(f"Your {user_Age}, you're too young to drink coffee ")
  exit() 
else :
  print(f"Hello {user_Name}, Welcome to the ARC mini Coffee shop \n \n")
  # If age is greater to 10 tutuloy  

list_of_coffee = (
  "Espresso",   # index 0 
  "Cappuccino", # 1 
  "Latte",      # 2 
  "Americano",  # 3
  "Mocha"       # 4 
)  # Tuple here

print(f"Menu:\nEspresso,\nCappuccino,\nLatte,\nAmericano,\nMocha")

Order = input("What is your order?: ")
quantity = int(input("How many?: "))

# Todo here 
if Order == "Espresso" : 
  price = 30 
  total = price * quantity 
  print(f"Your order is {quantity} pcs of {list_of_coffee[0]}, total of {total}. ")
elif Order == "Cappuccino" :
  price = 35 
  total = price + quantity 
  print(f"Your order is {quantity} pcs of {list_of_coffee[1]}, total of {total}. ")
elif Order == "Latte" :
  price = 35
  total = price + quantity 
  print(f"Your order is {quantity} pcs of {list_of_coffee[2]}, total of {total}. ")
