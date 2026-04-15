print("note: Enter the number of the desired operation.")

try:
    with open("message.txt", "x") as file:
        file.write("")
except FileExistsError:
    print("File already exists.")


while True:
    print("Welcome to Messaging App")
    print("1. Send Message")
    print("2. View Messages")
    print("3. Exit")
    operation = input("Enter choice: ")
    
    
    try:
        
        if operation == "1":
            with open("message.txt", "a") as file:
                message = input("Enter your message: ")
                file.write(message)
                print("Message sent!")
        elif operation == "2":
            with open("message.txt", "r") as file:
                print("---Messages---")
                print(file.read())
        elif operation == "3":
            print("Thank you and Good bye!")
            break
    except ValueError:
        print("Please enter a valid input.")
