a = int(input("Enter your age: "))
b = str(input("Do you have a degree(Yes or No): "))
c = float(input("Enter your work experience: "))
if a >=18:
 if b == "No":
    print("Not Eligible")

    if b == "Yes":


        if c>3:
            print("Highly Eligible")
        elif 1<=c<=3:
            print("Eligible")
        else:
            print("Under Review")
else:
    print("Not eligible")