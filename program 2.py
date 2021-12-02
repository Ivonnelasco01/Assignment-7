
# enter password
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char


#value

print(" Password validator ")
print("The password is valid if all criteria are met:")
print("a. Greater than 15 letters")
print("b. Have at least one capital letter")
print("c. Have at least one number")
print("d. Have at least one special char")
print(" ")

character = 0
uppercase = 0
number = 0
special = 0

while True:
    password = input("Enter your password here: ")
    for char in password:
        if len(password) > 15:
            character += 1
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase += 1
        if char in "0123456789":
            number += 1
        if char in "!@#$%^&*()_+-=,./;'[]<>?:{}\|":
            special += 1
    if character == 0:
        print("Password must be greater than 15 characters")
    elif uppercase == 0:
        print("Password must have at least one capital letter")
    elif number == 0:
        print("Have at least one number")
    elif special == 0:
        print("Have at least one special character")
    else:
        print("Password is valid")
        break
