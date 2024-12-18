a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = input("Enter a operator :")
if c == "+":
    r = (a+b)
elif c == "-":
    r = (a-b)
elif c == "*":
    r = (a*b)
elif c == "/":
    if b != 0:
      r = (a/b)
    else:
        print("Error")
elif c == "%":
    r = (a%b)
elif c == "**":
    r = (a**b)
elif c == "//":
    r = (a//b)
else:
    print("Error")
print(f"Your result is : {r}")
