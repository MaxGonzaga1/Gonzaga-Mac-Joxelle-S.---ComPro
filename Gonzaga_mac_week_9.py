myList = []

while True:
    print("Menu: ")
    print(" 1. Show Users \n 2. Add User \n 3. Update User \n 4. Delete User \n 5. Exit")

    operation = int(input("Select an Action: "))

    if operation == 1:
        print(myList)
    elif operation == 2:
        newUser = input("Enter new user: ")
        myList.append(newUser)
        print(myList)
    elif operation == 3:
        userIndex = int(input("Enter the index of the existing user: "))
        updateUser = input("Enter updated user: ")
        myList[userIndex] = updateUser
        print(f"Updated list of users: {myList}")
    elif operation == 4:
        existUser = input("Enter the existing user: ")
        myList.remove(existUser)
        print(f"Updated list of users: {myList}")
    elif operation == 5:
        print("goodbye!")
        break
    else:
        print("Enter a valid input.")