a = input("Enter a string: ")
r = ""
for i in range(len(a)):
    if i % 2 != 0:
        r += a[i]
print(f"Odd characters are {r}")