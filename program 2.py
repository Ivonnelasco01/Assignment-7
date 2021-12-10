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

def password_validator():
    while True:
        password = input("Please enter you password here: ")
        if len(password) < 15:
            print("Password must atleast 15 characters, one capital letter, one number, and one special character ")
        elif not "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("Password must atleast 15 characters, one capital letter, one number, and one special character ")
        elif not "0123456789":
            print("Password must atleast 15 characters, one capital letter, one number, and one special character ")
        elif not "!@#$%^&*()_+-=,./;'[]<>?:{}\|":
            print("Password must atleast 15 characters, one capital letter, one number, and one special character ")
        else:
            print("Your password is valid")
            break
password_validator()
