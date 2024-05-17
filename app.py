from database import


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
