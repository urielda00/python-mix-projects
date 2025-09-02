name = input("Hey type your name: ") 
print("Hello " + name + " welcome to my game!")

should_we_play = input("Do you want to play? ").lower()
if should_we_play== "y" or should_we_play == "yes":
  print("We are gonna play!")
  weapon = input("Choice a weapon (sword/axe): ").lower()

  direction = input("Do you want to go left or right? ").lower()
  if direction == "left":
    print("ok we went left")
  elif direction == "right":
    choice = input("Okay, now you see a bridge, do you want to swim under it or cross it? (swim/cross): ")
    if choice == "swim" and weapon == "axe":
      print("ok you survived!")
  else:
    print("sorry, not a valid input..")
else:
  print("We are NOT playing...")
