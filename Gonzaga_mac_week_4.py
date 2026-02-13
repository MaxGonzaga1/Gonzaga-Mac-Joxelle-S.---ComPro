#Log In System

#stored credentials
name = "Mac Gonzaga"
age = 19

#input name and age from user
name_input = input("Enter your name: ")
age_input = int(input("Enter your age: "))

#check if the input matches the stored credentials
if name_input == name and age_input == age:
    print("Log in successful!")
else:
    print("Log in failed. Please check your name and age.")

#End of program