from columnar import columnar


def print_list_ticket_info(field_names, tickets):
    """Function to print multiple tickets' information.
    Args:
        field_names (List[str]): List of fields/details we want to obtain from the tickets.
        tickets (List[json]): The list of tickets to print information from.
    """
    
    headers = field_names
    table = []

    for ticket in tickets:
        ticket_info = []
        for field in field_names:
            try:
                ticket_info.append(ticket[field])
            except:
                print("{} field is not available".format(field))
                return
        table.append(ticket_info)

    printable_table = columnar(table, headers, no_borders=False)
    print(printable_table)


def print_single_ticket_info(field_names, ticket):
    """Function to print a single ticket's information
    Args:
        field_names (List[str]): List of fields/details we want to obtain from the ticket.
        ticket (json): The ticket to print information from.
    """
    
    if 'error' in ticket.keys():
        print("Error: {}".format(ticket["error"]))
        return
    ticket_detail = ticket["ticket"]
    headers = field_names
    table = []
    ticket_info = []
    for field in field_names:    
        try:
            ticket_info.append(ticket_detail[field])
        except:
            print("{} field is not available".format(field))
            return
    table.append(ticket_info)

    printable_table = columnar(table, headers, no_borders=False)
    print(printable_table)
