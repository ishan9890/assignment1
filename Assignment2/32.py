print("Welcome to the Haunted House")
a = input("Do you want to go upstairs or downstairs?: ")
if a == "downstairs":
    print("Game Over")
elif a == "upstairs":
    c = input("Do you want to enter the room or stay outside?: ")
    if c == "enter the room":
        print("Game over")
    else:
        print("Invalid Operation!")
elif c == "stay outside":
        d = input("Choose between 'ghost', 'vampire', or 'werewolf': ")
        if d == "ghost" or "vampire":
            print("Game Over")
        elif d == "werewolf":
            print("You win!")
        else:
             print("Invalid operation!")
else:
    print("Invalid Operation!")