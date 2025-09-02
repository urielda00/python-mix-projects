import json

def addPerson():
  name = input("Name: ")
  age = input("Age: ")
  email = input("Email: ")

  # return the created person:
  return {"name" : name, "age":age,"email":email}

def displayPeople(people):
  for i, person in enumerate(people):
    print(i+1,"-",person["name"],"|",person["age"],person["email"])

def deleteContact(people):
  displayPeople(people)
  while True:
    number = input("Enter a number to delete: ")
    try:
      number = int(number)
      if number <= 0 or number > len(people):
        print("Invalid number, out of range.")
      else:
        break
    except:
      print("Invalid number.")
  people.pop(number-1)
  print("Person deleted")

def search(people):
  search_name = input("Search for a name: ").lower()
  results = []

  for person in people:
    name = person["name"]
    if search_name in name.lower():
      results.append(person)
  displayPeople(results)

print("Hi, welcome to the contact management system")
print()

# read mode:
with open("contacts.json","r") as f:
  people = json.load(f)["contacts"]

while True:
  print()
  print("Contact list size:", len(people))
  command = input("You can 'Add', 'Delete', or 'Search' and Q for quit: ").lower()

  if command == "add":
    person = addPerson()
    people.append(person)
    print("person added")
  elif command == "delete":
    deleteContact(people)
  elif command == "search":
    search(people)
  elif command == "q":
    break
  else:
    print("Invalid command")

# write mode:
with open("contacts.json","w") as f:
  json.dump({"contacts":people},f)