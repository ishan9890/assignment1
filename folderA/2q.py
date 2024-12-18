print("Welcome to Treasure Land")
a = str(input("Choose a Direction(left or right): "))

if a == "right":
    print("Game Over")

elif a == "left":
    b =str(input("swim or wait:"))
    if b == "swim":
        print("Game Over")
    elif b == "wait":
        c = (input("Choose a colour: "))
        if c == "red" or  c =="blue":
            print("Game Over")
        elif c == "yellow":
            print("You Win")
else:
    print("invalid")

