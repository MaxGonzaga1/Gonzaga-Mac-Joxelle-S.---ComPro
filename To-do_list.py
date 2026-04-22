try:
    with open ("tasks.txt","x") as file:
        print(file.write("Existing tasks:"))
except:
    print("file already exist.")

    
print("note: enter the number of the operation.")
while True:
    print("""
    To do list system operations:
    1. Add task
    2. View existing tasks
    3. Exit
    """)
    try:
        operation = input("enter operation: ")
        if operation == "1":
            try:
                Task = input("Enter new task: ")
                with open ("tasks.txt","a") as file:
                    file.write(f"\n- {Task}")
                    print(f"new task added: {Task}")
            except FileNotFoundError:
                print("file not found.")
        elif operation == "2":
            try:
                with open ("tasks.txt","r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("file not found.")
        elif operation == "3":
            print("Thank you and good bye!")
            break
        else:
            print("Please input a valid operation.")
    except ValueError:
        print()
