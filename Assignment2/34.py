print("Welcome to the Magic Forest")
a = input("Do you want to go north or south?")
if a =="south":
    print("Game over")
elif a == "north":
    b = input("Do you want to cross the river or follow the path?: ")
else:
    print("Invalid")
if b == "cross the river":
    print("Game over")
elif b == "follow the path":
    c = input("Choose between 'fairy,'ogre','elf': ")
else:
    print("Invalid")
if c == "fairy" or "ogre":
    print("Game Over")
elif c == "elf":
    print("You Win")
else:
    print("Invalid")
    