from database import Database

def print_menu():
    """
    register a member, view registered members.
    Also, you have options to update and delete members.
    :return:
    """
    print("""
    1-Sign up for membership.
    2-Show all members.
    3-Update registered members.
    4-Delete registered members.
    """)


def get_valid_choice():
    """
    select the operation admin want to perform.
    :return:
    """
    while True:
        admin_choice = input("Please select you want to perform.")
        if not admin_choice.isdigit():
            print("Please enter a valid number.")
            admin_choice = int(admin_choice)
            if admin_choice not in [1 ,2, 3, 4]:
                print("Please enter a valid number.")
            else:
               return admin_choice


def get_valid_input(prompt):
    while True:
        admin_input = input(prompt).strip()
        if not admin_input:
            print("Please enter a value.")


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
    '''
    Example:
    1 month => 100 dollar
    3 month => 250 dollar
    6 month => 450 dollar
    12 month => 800 dollar
    '''
    price = int(get_valid_input("Package Price: "))
    duration = int(get_valid_input("Duration(in months): "))

    # use Database class to add members.
    db = Database()
    db.add_member(name, last_name, age, city, price, duration)
    print("Member added successfully!")

elif choice == 2:
    '''
    Show registered members.
    '''
    db = Database()
    members = db.get_members()
    for member in members:
        print(member)

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

    # Check. Is there an ID or not ??
    is_member = False
    for member in members:
        if member[0] == member_id:
            is_member = True
            break

    if is_member:
        """ 
        Put new info for the member
        """
        # name, last_name, age, city, price, duration
        # [ db.update_member(...) ]
        # Member information updated successfully!
        # else: Member with ID {member_id} does not exist!


elif choice == 4:
    '''
    Delete a member.
    '''
    pass

else:
    print("Choice is invalid. Please try again.")