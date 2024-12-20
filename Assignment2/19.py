a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
o = input("Enter a operator(+,-,*,/): ")
if o == "+":
    r = a+b
elif o == "-":
        r = a-b
elif o == "*":
            r = a*b
elif o == "/":
         r = a/b
         if b == 0:
                 print("Invalid!")
print(f"Your result is: {r}")

