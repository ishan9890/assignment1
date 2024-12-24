print("Welcome to the forest adventure")
a = str(input("Choose 'left' or 'right': "))
if a == "left":
    b = input("Pick between 'explore' or 'rest': ")
    if b == "explore":
        print("You found treasure")
    elif b == "rest":
        print("You were attacked by wild animals. Game Over")
    else:
        print("Invalid")
elif a == "right":
    print("You fell into a trap.Game Over")
else:
    print("Invalid")