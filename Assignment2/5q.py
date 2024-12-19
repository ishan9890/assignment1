print("Enter your marks!")
s1 = float(input("Subject 1:"))
s2 = float(input("Subject 2:"))
s3 = float(input("Subject 3:"))
s4 = float(input("Subject 4:"))
t = s1+s2+s3+s4
p = (t/400)*100
if p>70:
    print("Distinction")
elif p>60:
    print("First Division")
elif p>40:
    print("Pass")
else:
    print("Fail")
print("\nResults")
print(f"Total Marks = {t}")
print(f"Percentage = {p}%")
