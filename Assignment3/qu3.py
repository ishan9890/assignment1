a = int(input("Enter your monthly salary: "))
if a >50000:
    print("High Earner")
elif a<=50000:
    b = int(input("Is your salary more than 20000: "))
    if b == "Yes":
        print("Mid earner")
else:
    print("Low earner")
