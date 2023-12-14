# Initialize lists to store names and contact numbers
names = [
    ["michael", "branson"],
    ["john", "doe"],
    ["jane", "smith"],
    ["emily", "jones"]
]
contact_number = [
    "456-433-4334",
    "123-456-7890",
    "987-654-3210",
    "555-123-4567"
]

def add_contact():
    # List of possible actions
    selection = ["add", "search", "delete", "list"]

    # Prompt the user for what action they want to perform
    response = input("Would you like to add, search, delete, or list a contact?: ").lower().strip()

    if response == "add":
        # If 'add' is selected, get first name, last name, and phone number from user
        add_first = input("Please enter in a first name first: ").lower().strip()
        add_last = input("Please enter in a last name: ").lower().strip()
        add_phone_number = input("Please enter in a phone number following \"***-***-****\" format: ")
        
        # Append the new contact to the names and contact_number lists
        names.append((add_first, add_last))
        contact_number.append(add_phone_number)
        
        # Confirm to the user that the contact has been added
        print("You have successfully added " + str(add_first) + " " + str(add_last))

    elif response == "search":
        # If 'search' is selected, ask for the phone number to search for
        search = input("Please type the phone number of the person you are trying to search: ")
        if search in contact_number:
            # Find the index of the phone number and display the corresponding name
            index = contact_number.index(search)
            called_names = names[index]
            called_number = contact_number[index]
            print("This is " + " ".join(called_names) + " and their phone number is " + called_number)

    elif response == "delete":
        # If 'delete' is selected, ask for the phone number to delete
        delete = input("Please type the phone number of the person you are trying to delete: ")
        if delete in contact_number:
            # Find the index of the phone number, delete both the name and phone number
            index = contact_number.index(delete)
            contact_number.pop(index)
            names.pop(index)
            # Confirm to the user that the contact has been deleted
            print("Contact deleted successfully.")

    elif response == "list":
        # If 'list' is selected, print all contacts
        print("This is your full contact list: " + str(names) + ", " + str(contact_number))

    else:
        # If the response is not recognized, inform the user
        print("Invalid option selected.")

# Call the function to add, search, delete, or list contacts
add_contact()
