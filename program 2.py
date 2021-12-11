# enter password
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char
import re

print(" Password validator ")
print("The password is valid if all criteria are met:")
print("a. Greater than 15 letters")
print("b. Have at least one capital letter")
print("c. Have at least one number")
print("d. Have at least one special char")
print(" ")

p = input("Enter your password here")
x = True
while x:      
    if (len(p)<15):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Password is valid")
        x=False
        break

if x:
    print("Password is not valid")
