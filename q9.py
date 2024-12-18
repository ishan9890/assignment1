a = str(input("Enter a Character:"))
if len(a)==1 and a.isalpha:
    if a in "aeiou":
     print("vowel")
else:
    print("consonent")