balance = 5000
print("Welcome to the ATM!")
print("1.Balance Inquiry")
print("2. Withdraw Cash")
print("3. Deposit Cash")
print("4. Exit")
choice = int(input("Please enter your choice (1-4): "))
if choice == 1:
    print(f"Your current balamce is: {balance}")

elif choice == 2:
    amount = int(input("Enter the amount to withdraw: "))
    if amount>balance:
        print("Insufficent balance.")
    else:
        balance -= amount
        print(f"Withdraw Succesfull Your new balnce is: ${balance}")
elif choice == 3:
    amount = int(input("Enter the amount to deposit: "))
    if amount <=0:
        print("Invalid amount. Please enter a positive value. ")
    else:
        balance += amount
        print(f"Deposit successful Your new balanc is: ${balance}")
elif choice == 4:
    print("Thank you for using the ATM. GoodBye!")

else:
    print("Invalid Choice! Please try again.")