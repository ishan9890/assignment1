print("Welcome to the Jungle Survival Challenge")
print("1.Search for food")
print("2.Build a shelter")
a = int(input("Choose between 1 & 2: "))
if a == 1:
    print("1.Hunt")
    print("2.Gather")
    b = int(input("Choose between 1 & 2: "))
    if b == 1:
        print("You were attacked by a wild animal. Game Over")
    elif b == 2:
        print("You found enough food.You Win!")
    else:
        print("Invalid!")
elif a == 2:
    print("Your shelther collapsed in the rain.Game Over")
else:
    print("Invalid!")