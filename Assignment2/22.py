a = str(input("Enter your gender: "))
b = int(input("Enter your age: "))
if 18<=b<30:
    if a == "M":
        print("Your wage is Rs.700")
    elif a == "F":
        print("Your wage is Rs.750")
    else:
        print("Invalid!")
if 30<=b<=40:
    if a == "M":
        print("Your wage is Rs.800")
    elif a == "F":
        print("Your wage is Rs.850")
    else:
        print("Invalid!")