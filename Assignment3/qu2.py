a = str(input("Choose vegetarian or non-vegetarian: "))
if a =="vegetarian":
    b = input("Salad or Pasta: ")
elif a == "non-vegetarian":
    b = input("Chicken or Fish: ")
else:
    print("Not Available!")
print(f"You have choosen {b}")
