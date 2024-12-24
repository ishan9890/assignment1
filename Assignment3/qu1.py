a = int(input("Enter the price of an item: "))
if a >1000:
    d = (a*10)/100
elif 5000<a<=10000:
    d = (a*5)/100
else:
    d = 0
p = a - d
print(f"The final price is: {p}")