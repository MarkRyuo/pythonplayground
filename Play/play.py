# person = {
#   "name": "Jhon Mark",
#   "age" : 21,
#   "online" : True,
#   "askOf" : lambda : print("Konichiwa Jhon Mark Desu!")

# }

# def user_Person(person) :
#   login = person["name"]
#   online = person["online"]
#   print(f"Hey, you log in successfully user {login} and you are online: {online}")
  
# user_Person(person) 

# todo Character Selection 
#Object 
character1 = {
  "name": "Mark",
  "age" : 18,
  "status" : True  
}

character2 = {
  "name" : "Nicole",
  "age" : 18,
  "status" : True 
}

# name , age , status 

# character = "" ;

# while len(character) == 0 :
#   character = input("Enter a name: ")

# print(f"Hello {character}") 


character = input("Enter your name: ")

while not character :
  character = input("Enter your name: ")
print(f"Hello {character}") 