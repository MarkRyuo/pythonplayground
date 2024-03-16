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



user_Age = int(input("What is your age: \n"))

# Condition if age is less than or equal to 10 : too young to drink coffee
if user_Age <= 10 : 
  print(f"Your {user_Age}, you're too young to drink coffee ")
  exit() 
else :
  print(f"Hello {user_Name}, Welcome to the ARC mini Coffee shop \n \n")
  # If age is greater to 10 tutuloy  

list_of_coffee = (
  "Espresso", 
  "Cappuccino", 
  "Latte", 
  "Americano", 
  "Mocha"
)  # Tuple here

print(f"Menu:\nEspresso,\nCappuccino,\nLatte,\nAmericano,\nMocha")

Order = input("What is your order?: ")


