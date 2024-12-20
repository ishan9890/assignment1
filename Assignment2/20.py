a = int(input("Enter the total number of days: "))
b = int(input("Enter total number of absent days: "))
ad = a-b
p = (ad/a)*100
print(f"Your attendance is {p:.3f}%")
if p>75:
    print("You are able to sit in the exam!")
else:
    print("You are not able to sit in the exam!")
