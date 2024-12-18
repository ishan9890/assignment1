a = int(input("Enter your salary: "))
b = int(input("Enter your period of service: "))
if b>5:
    bo = 5
else:
    print("You can't receive bonus!")
bn = (bo/100)*a
print(f"The net bonus amount is Rs.{bn}")