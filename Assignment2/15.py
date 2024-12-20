N = int(input("Enter the number of students: "))
K = int(input("Enter the number of apples: "))
aps = K//N
ra = K % N
print(f"Each student will get {aps} apples")
print(f"{ra} apples will remain in the basket")
