#Log In System

#stored credentials
name = "Mac Gonzaga"
password = "user1234"

#input name and password from user
name_input = input("Enter your name: ")
password_input = input("Enter your password: ")

#check if the input matches the stored credentials
if name_input == name and password_input == password:
    print("Log in successful!")
else:
    print("Log in failed. Please check your name and password.")

#End of program