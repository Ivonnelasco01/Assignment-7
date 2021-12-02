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

user_password = input("Enter your password here: ")
password_validator = True

while password_validator:
    # a. Greater than 15 letters
    if (len(user_password)<15):
        print("Password must contain greater than 15 character")
        break
    



