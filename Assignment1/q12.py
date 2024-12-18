a = str(input("Enter a character:"))
if a.isupper():
    print(f"{a} is an uppercase letter")
elif a.islower():
    print(f"{a} is a lowercase letter")
elif a.isdigit():
    print(f"{a} is a digit")