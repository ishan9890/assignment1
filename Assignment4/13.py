a = input("Enter a string: ")
r = ""
for i in range(len(a)):
    if i % 2 ==0:
        r += a[i]
print(f"Even characters are {r}")