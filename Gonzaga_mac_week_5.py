#password validation program

#users input a password
fromUser = input("Enter a password: ")

#conditions for a valid password
any(char.isalpha() for char in fromUser) >= 1
any(char.isdigit() for char in fromUser) >= 1
len(fromUser) >= 8

#printing the result of the password validation
if any(char.isalpha() for char in fromUser) and any(char.isdigit() for char in fromUser) and len(fromUser) >= 8:
    print("Your password is accepted.")
else:    print("Your password is invalid. It must contain at least one letter, one number, and be at least 8 characters long.") 

while True:
    from_user = input("Enter your password: ")
    
    letters = any(chr.isalpha()for chr in from_user) 
    numbers = any(chr.isdigit()for chr in from_user)
    sizes = len(from_user) > 8
    
    if letters and numbers and sizes:
        print("Password accepted.")
    else:
        print("Password is invalid, Please try again.")