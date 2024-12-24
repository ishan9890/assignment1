print("Welcome to the Jungle Adventure")
a = input("Do you want to go left or right?: ")
if a == "right":
    print("Game Over")
elif a == "left":
    b = input("Do you want to climb a tree or explore the cave?: ")
else:
    print("Invalid")
if b == "climb a tree":
    print("Game Over")
elif b == "explore the cave":
    c = input("Choose between 'bear', 'tiger' , or 'snake': ")
else:
    print("Invalid")
if c == "bear" or "tiger":
    print("Game Over")
elif c == "snake":
    print("You Win")
else:
    print("Invalid")
