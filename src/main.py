from api import get_all_tickets, get_ticket_detail, get_paging, get_total_page
from helper import print_list_ticket_info, print_single_ticket_info

valid_input = ["1", "2", "quit"]

def validInput(user_text):
    """Function to verify if a user input is valid.
    Args:
        user_text (str): User-entered input.
    Returns:
        bool: Whether or not the input is valid.
    """
    
    return user_text in valid_input

def view_all_ticket(user_text):
    """Function to check if user command is to view all tickets.
    Args:
        user_text (str): User-entered input.
    Returns:
        bool: Whether or not the input corresponds to the key for viewing all tickets.
    """
    
    return user_text == "1"

def view_single_ticket(user_text):
    """Function to check if user command is to view a single ticket.
    Args:
        user_text (str): User-entered input.
    Returns:
        bool: Whether or not the input corresponds to the key for viewing single ticket.
    """
    
    return user_text == "2"

def quit(user_text):
    """Function to check if user command is to quit.
    Args:
        user_text (str): User-entered input.
    Returns:
        bool: Whether or not the input corresponds to the key for quitting the application.
    """

    return user_text == "quit"

def is_cancelled(page_number_input):
    """Function to check if user command is to stop viewing ticket pages.
    Args:
        user_text (str): User-entered input.
    Returns:
        bool: Whether or not the input corresponds to the key for cancelling viewing.
    """
    
    return page_number_input == 'c'
    
def is_valid_page(page_number, total_page):
    """Function to check if an entered page number is valid.
    Args:
        page_number (int): User-entered page number to see tickets from.
        total_page ([type]): Total number of pages that index the tickets.
    Returns:
        bool: Whether the page number is invalid (out of bounds).
    """
    
    return page_number > total_page or page_number <= 0

def show_all_tickets():
    """Function to process user command of viewing all tickets.
    """
    
    all_tickets = get_all_tickets()
    total_page = get_total_page(len(all_tickets))
    page_number = 1
    print_list_ticket_info(["id", "status", "subject", "created_at"], get_paging(page_number, all_tickets))
    page_number_input = input("This is page {} of {}. Which page do you want to view? Type page number or c for cancel: ".format(page_number, total_page))
    while (not is_cancelled(page_number_input)):
        try:
            page_number = int(page_number_input)
            if is_valid_page(page_number, total_page):
                print("Invalid page number. There are only {} pages from 1 to {} ".format(total_page, total_page))
            else:
                print_list_ticket_info(["id", "status", "subject", "created_at"], get_paging(page_number, all_tickets))
        except ValueError:
            print("Page number must a number, try again")
        
        page_number_input = input("There is a total of {} pages. Which page do you want to view? Type page number or c for cancel: ".format(total_page))

def show_single_ticket():
    """Function to process user command of viewing a single ticket.
    """
    
    try:
        ticket_id = int(input("Ticket number: "))
        print_single_ticket_info(
            ["id", "status", "subject", "created_at"], get_ticket_detail(ticket_id)
        )
    except ValueError:
        print("Ticket number must a number, try again")

if __name__ == "__main__":
    print("Hello, welcome to ticket information site.")
    user_text = input("Type 1 to view all tickets, 2 to view one, quit to quit the application: ")
    while not quit(user_text):
        if not validInput(user_text):
            print("Invalid input, try again")
        if view_all_ticket(user_text):
            show_all_tickets()   
        elif view_single_ticket(user_text):
            show_single_ticket()
        user_text = input("Type 1 to view all tickets, 2 to view one, quit to quit the application: ")
    print("Goodbye!")
