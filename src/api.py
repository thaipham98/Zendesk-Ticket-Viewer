import requests
from requests.auth import HTTPBasicAuth
import json
import math

from requests.models import HTTPError


USER_NAME = "giathai1998@gmail.com"
PASSWORD = "Se?ajTsavRCY7J!"
URL = "https://zcc9334.zendesk.com/api/v2"
LIMIT = 25

def validate_response(response):
    if response.status_code == 500:
        raise HTTPError("Code {}, {}.".format(response.status_code, response.reason))
        
def get_all_tickets():
    """Function to obtain all tickets from HTTP requests.
    Returns:
        List[json]: List of ticket data obtained.
    """
    
    data = []
    page = 1
    response = requests.get(
        "{}/tickets?page={}".format(URL, page),
        auth=HTTPBasicAuth(USER_NAME, PASSWORD),
    )
    
    validate_response(response)

    parsed_response = json.loads(response.text)
    next_page = parsed_response["next_page"]
    for ticket in parsed_response["tickets"]:
        data.append(ticket)

    while next_page != None:
        page += 1
        response = requests.get(
            "{}/tickets?page={}".format(URL, page),
            auth=HTTPBasicAuth(USER_NAME, PASSWORD),
        )
        parsed_response = json.loads(response.text)
        for ticket in parsed_response["tickets"]:
            data.append(ticket)
        next_page = parsed_response["next_page"]

    return data

def get_total_page(total_tickets):
    """Function to get total number of pages that indexes the tickets.
    Args:
        total_tickets (int): Total number of tickets
    Returns:
        int: Number of pages to index the tickets.
    """

    return math.ceil(total_tickets / LIMIT) 

def get_paging(page_number, tickets):
    """Function to get all ticket data from a specified page.

    Args:
        page_number (int): The page index to get tickets from.
        tickets (List[json]): All tickets that are indexed through pages.
    Raises:
        ValueError: If the specified page number argument is invalid.

    Returns:
        List[json]: All ticket data in the given page.
    """
    
    total_ticket = len(tickets) 
    total_page = math.ceil(total_ticket / LIMIT) 
    
    if page_number > total_page:
        raise ValueError("Invalid page number. There are only {} pages".format(total_page))
            
    data = []
    
    if page_number * LIMIT <= total_ticket:
        ending = page_number * LIMIT - 1 
        starting = page_number * LIMIT - LIMIT  
    else: 
        ending = total_ticket - 1 
        starting = total_ticket - total_ticket % LIMIT  
    
    for i in range(starting, ending + 1, 1):
        data.append(tickets[i])
    
    return data
    
def get_ticket_detail(ticket_id):
    """Function to get a specified ticket's details
    Args:
        ticket_id (int): ID of the wanted ticket.
    Returns:
        Dict[int, str]: The ticket's full details.
    """
    
    response = requests.get(
        "{}/tickets/{}".format(URL, ticket_id),
        auth=HTTPBasicAuth(USER_NAME, PASSWORD),
    )
    
    validate_response(response)
    
    parsed_response = json.loads(response.text)

    return parsed_response
