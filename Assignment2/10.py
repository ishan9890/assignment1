a = float(input("Enter your time period of service: "))
s = float(input("Enter your salary: "))
if a>10:
    b = 10
elif 6<=a<=10:
    b = 8
elif a<6:
    b = 5
br = (b/100)*s
print("\n Bonus Received: ")
print(f"Your time period of service is: {a} years")
print(f"Your Salary is: Rs.{s}")
print(f"You have received {b}% bonus")
print(f"You will receive Rs. {br} as bonus")


