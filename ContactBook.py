import json

try:
  with open("BeginnerProjects/Contacts.json","r") as file:
    contact = json.load(file)
except FileNotFoundError:
  contact = {}

def save_name():

  name = input("Enter Name:\n")

  phone_number = input("Enter Phone Number:\n")

  email_id = input("Enter email id:\n")

  contact[name] = {"Phone Number": phone_number, "Email id": email_id}

  with open("BeginnerProjects/Contacts.json","w") as file:
    json.dump(contact,file)



def delet_name():
  name = input("Enter name of the contact to delet: ")
  if name in contact:
    del contact[name]
    with open("BeginnerProjects/Contacts.json","w") as file:
      json.dump(contact,file)
  else :
    print("Name not found: ")

def view_names():
  for number,(key, values) in enumerate(contact.items(), start=1):
    print(f"{number}.{key}")
    print(f"Phone Number : {values['Phone Number']}")
    print(f"Email Id : {values['Email id']}")
    print("\n")

def search_name():
  name = input("Enter name to search: ")
  if name in contact:
    print("\n")
    print(name)
    print(f"Phone Number: {contact[name]['Phone Number']}")
    print(f"Email Id : {contact[name]['Email id']}")
    print("\n")
    

  else:
    print("Contact not found")
    print("\n")

choiceList = ["1. View Contacts","2. Add a Contact","3. Delet a contact","4. Search Contact","5. Exit"]


while True:
  for i in choiceList:
    print(i)

  choice = int(input("Enter the choice: "))

  match choice:
    case 1:
      view_names()
    case 2:
      save_name()
    case 3:
      delet_name()
    case 4:
      search_name()
    case 5:
      break
    case _:
      choice = int(input("Enter a valid choice: "))
