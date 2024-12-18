a = float(input("Enter your marks:  "))
if a<25:
    g = "D"
elif 25<=a<=44:
    g ="C"
elif 45<=a<=49:
    g ="B"
elif 50<=a<=59:
    g ="B+"
elif 60<=a<=79:
    g = "A"
elif a>80:
    g ="A+"
print(f"Your grade is: {g}")
