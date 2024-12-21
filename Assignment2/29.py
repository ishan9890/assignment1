a = float(input("Enter the weight of the package(in kg): "))
i = input("Is the delivery urgent? (yes/no): ")
if a <5:
    c = 5
elif 5<=a<=20:
    c = 10
else:
    c = 20
if i == "yes":
    c = c +5
print(f"The delivery cost of the package is ${c}")
