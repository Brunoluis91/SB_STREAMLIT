
from constants import COSTS

def calculate_cost(selected_services, area=0):
    """ Calculate the total cost based on selected services and area.
    
    :param selected_services: List of services selected by the user.
    :param area: Area in square meters for services like painting. Default is 0.
    :return: Total cost for the selected services.
    """
    total_cost = 0
    
    for service in selected_services:
        if service == 'PAINT':
            total_cost += COSTS[service] * area
        else:
            total_cost += COSTS[service]
    
    # Apply the 10% service charge
    total_cost += total_cost * 0.10
    
    return total_cost
