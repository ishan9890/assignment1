print("Welcome to the Haunted House")
a = input("Do you want to go upstairs or downstairs?: ")
if a == "downstairs":
    print("Game Over")
elif a == "upstairs":
    b = input("Do you want to enter the room or stay outside?: ")
    if b == "enter the room":
        print("Game over")
    elif b == "stay outside":
        c = input("Choose between 'ghost','vampire', or 'werewolf': ")
        if c in ["ghsot" , "vampire"]:
            print("Game Over")
        elif c == "werewolf":
            print("you win")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")

    
