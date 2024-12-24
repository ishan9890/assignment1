n = input("Enter an integer: ")
r = ""
for i in range(len(n)-1,-1,-1):
    r += n[i]
print(f"Original Integer: {n}")
print(f"Reversed Integer: {r}")

