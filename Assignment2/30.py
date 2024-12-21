a = int(input("Enter your income: "))
if a>50000:
    c = int(input("Enter your credit score: "))
    if c>700:
        print("Loan approved")
    elif 600<=c<=700:
        print("Higher interest rate will be applied in the loan")
    else:
        print("Loan Rejected")
else:
    print("Loan Rejected")
    