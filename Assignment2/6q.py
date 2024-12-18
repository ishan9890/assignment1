a = int(input("Enter the cost price(in Rs.): "))
if a>100000:
    t = 15
elif 50000<a<=100000:
    t = 10
elif a<=50000:
    t = 5
b = (t/100)*a
print("\nRoad Tax Details")
print(f"Cost Price: {a}")
print(f"Tax rate: {t}")
print(f"Road tax to be paid: {b}")

