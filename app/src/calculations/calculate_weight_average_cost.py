

def calculate_weight_average_cost(stocks_transactions, weight_average_cost, current_quantity):
    """
    Calculate the weighted average cost for each stock transaction in the provided list.

    Parameters:
    - stocks_transactions (list of dict): List of stock transaction dictionaries, where each dictionary contains
      information about a single transaction, including "unit-cost" and "quantity".

    Returns:
    - list of dict: List of stock transaction dictionaries with an additional key "weight_average_cost"
      representing the calculated weighted average cost for each transaction.
    """

    weight_average_cost = calculate_new_weight_average_cost(stocks_transactions, weight_average_cost, current_quantity)
    return stocks_transactions, weight_average_cost


def calculate_new_weight_average_cost(transaction, weight_average_cost, current_quantity):
    """
    Calculate the new weighted average cost for each stock transaction in the provided list.

    This function updates the "weight_average_cost" key in each transaction dictionary based on the current
    quantity of stocks and the new transaction.

    Parameters:
    - stocks_transactions (list of dict): List of stock transaction dictionaries, where each dictionary contains
      information about a single transaction, including "operation", "quantity", "unit-cost", and "weight_average_cost".

    Returns:
    - list of dict: List of stock transaction dictionaries with updated "weight_average_cost" based on the new
      transaction and current quantity of stocks.
    """
    new_weight_average_cost = 0
    if transaction["operation"] == "buy":
        new_weight_average_cost = ((current_quantity * weight_average_cost) + (transaction["quantity"] * transaction["unit-cost"])) / (current_quantity + transaction["quantity"])
    return new_weight_average_cost


def define_weight_average_cost(operation, weight_average_cost, current_quantity):

    """
    Update the weighted average cost and current quantity based on the given operation.

    Parameters:
    - operation (dict): Dictionary representing a stock transaction operation.
    - weight_average_cost (float): The current weighted average cost of the stocks.
    - current_quantity (int): The current quantity of stocks.

    Returns:
    - tuple: A tuple containing the updated weighted average cost and current quantity.

    """
    if current_quantity == 0 and operation["operation"] == "buy":
        weight_average_cost = operation["unit-cost"]
        current_quantity = operation["quantity"]
    elif current_quantity > 0 and operation["operation"] == "buy":
        wac_stock_operation_list, weight_average_cost = calculate_weight_average_cost(
            operation, weight_average_cost, current_quantity)
    return weight_average_cost, current_quantity
