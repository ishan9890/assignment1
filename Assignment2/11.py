d = int(input("Enter the number of days the book is kept: "))
if d<=5:
    f = d*2
elif 6<=d<=10:
    f =(5*2)+(d-5)*3
elif 11<=d<=15:
    f = (5*2)+(5*3)+(d-10)*4
elif d>15:
    f = (5*2)+(5*3)+(5*4)+(d-15)*4
print(f"You have been charged Rs.{f}")