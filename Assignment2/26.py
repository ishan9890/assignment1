a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a>b:
    print(f"{a} is greater than {b}")
elif b>a:
    print(f"{b} is greater than {a}")
if a == b:
    if a >0 and b>0:
        print("The number is positive!")
    elif a<0 and b<0:
        print("The number is negative!")
    elif a==0 and b==0:
        print("The number is zero!")
