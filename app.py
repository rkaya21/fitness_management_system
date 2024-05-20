from database import Database

def print_menu():
    print("""
    1-Sign up for membership.
    2-Show all members.
    3-Update registered members.
    4-Delete registered members.
    """)

def get_valid_choice():
    while True:
        admin_choice = input("Please select what you want to perform: ")
        if admin_choice.isdigit():
            admin_choice = int(admin_choice)
            if admin_choice in [1, 2, 3, 4]:
                return admin_choice
            else:
                print("Please enter a valid number.")
        else:
            print("Please enter a valid number.")

def get_valid_input(prompt):
    while True:
        admin_input = input(prompt).strip()
        if admin_input:
            return admin_input
        else:
            print("Please enter a value.")

# Main loop
while True:
    print_menu()
    choice = get_valid_choice()

    if choice == 1:
        '''
        Sign up for membership
        '''
        name = get_valid_input("Member Name: ")
        last_name = get_valid_input("Member Last Name: ")
        age = int(get_valid_input("Member Age: "))
        city = get_valid_input("Member City: ")
        price = int(get_valid_input("Package Price: "))
        duration = int(get_valid_input("Duration(in months): "))

        db = Database()
        db.add_member(name, last_name, age, city, price, duration)
        print("Member added successfully!")
        break

    elif choice == 2:
        '''
        Show registered members.
        '''
        db = Database()
        members = db.get_members()
        for member in members:
            print(member)
        break

    elif choice == 3:
        '''
        Update registered members.
        '''
        db = Database()
        members = db.get_members()
        print("Registered members of list:")
        for member in members:
            print(member)

        member_id = int(get_valid_input("Enter ID of member you want to update: "))

        is_member = False
        for member in members:
            if member[0] == member_id:
                is_member = True
                break

        if is_member:
            name = get_valid_input("Update name: ")
            last_name = get_valid_input("Update last name: ")
            age = int(get_valid_input("Update age: "))
            city = get_valid_input("Update city: ")
            price = int(get_valid_input("Update price: "))
            duration = int(get_valid_input("Update duration(in months): "))

            db.update_member(member_id, name, last_name, age, city, price, duration)
            print("Member information updated succesfully")
        else:
            print(f"Member with ID {member_id} does not exist.")
        break

    elif choice == 4:
        '''
        Delete a member.
        '''
        db = Database()
        members = db.get_members()
        print("Registered members of list:")
        for member in members:
            print(member)

        member_id = int(get_valid_input("Enter ID of member you want to delete: "))

        is_member = False
        for member in members:
            if member[0] == member_id:
                is_member = True
                break

        if is_member:
            db.delete_member(member_id)
            print(f"Member with ID {member_id} deleted successfully.")
        else:
            print(f"Member with ID {member_id} does not exist.")
        break

    else:
        print("Choice is invalid. Please try again.")
