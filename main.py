
# Todo Arrays 
# list [] - Changeable 
# tuple () - Unchangeable 
# set {} - Unchangeable 
# dict {"name": "Jhon Mark"} - Changeable 

thislist  = ["apple", "mango", "cherry"]
def thisislist(thislist) :
  print(f"List of fruits: {thisislist}")
#add item in list 
  addinlist = input("Enter a fruit: ")
  thislist.append(addinlist)
  print(f"New list of fruits: {thisislist} ")

thisislist(thislist)