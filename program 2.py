
# enter password
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char


print(" Password validator ")
print("The password is valid if all criteria are met:")
print("a. Greater than 15 letters")
print("b. Have at least one capital letter")
print("c. Have at least one number")
print("d. Have at least one special char")
print(" ")

password = input("Enter your password here: ")
uppercase = False
number = False
special = False


for char in password:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXXYZ":
        uppercase = True
    elif char in "0123456789":
        number = True
    elif char in "~!#$%^&*()_+=-:;,.<>?/;'[]{}":
        special = True

if len(password) < 15:
    print("a. Greater than 15 letters")

if uppercase == False:
    print("b. Have at least one capital letter")

if number == False:
    print("c. Have at least one number")

if special == False:
    print("d. Have at least one special character")





