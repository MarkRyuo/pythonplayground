# Todo create a coffee shop 


# Todo create log-in for user, admin and staff / employee 

list_of_user = [
  "user1",
  "user2",
  "user3", 
  "user4", 
  "user5"
] # List 

list_of_employee = [
  "user1",
  "user2",
  "user3",
  "user4", 
  "user5"
] # List 

list_of_admin = (
  "admin1",
  "admin2",
  "admin3",
  "admin4"
) # Tuple

user = ""

def userOf() :
  while user == 0 :
    user = input("Are you ? Pick 1: (user, staff, Employee): ")
  return user 

if user == "user" :
  print("Log in to user")
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  if username == "user1" :