def rental_car_cost(days):
    """
    Calculate the cost of renting a car for a given number of days.

    Args:
        days (int): The number of days to rent the car.

    Returns:
        float: The total cost of renting the car, after any applicable discounts are applied.
    """
    cost = 40 * days

    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20

    return cost

# Example usage
total_cost = rental_car_cost(4)
print(total_cost)