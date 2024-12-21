a = str(input("Enter the weather: "))
if a == "sunny":
    print("You can enjoy outdoor activities like  visiting a nearby mall or hiking")
elif a == "rainy":
    c = input("Do you have a raincoat or umbrella?(yes/no): ")
    if c == "yes":
        print("You can go to a nearby mall or go hiking")
    elif c == "no":
        print("You should stay at home and watch movies")
else:
    print("I can't recommend for that option.")