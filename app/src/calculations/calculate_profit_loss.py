
from src.calculations.calculate_weight_average_cost import define_weight_average_cost


def calculate_profit_loss(transaction, weight_average_cost, current_quantity, cumulative_loss):
    """
    Calculates the total profit or loss from stock transactions.

    Parameters:
        - stocks_transactions (list): A list of stock transactions, where each transaction is a dictionary containing
        - information about the operation, unit cost, and quantity.

    Returns:
        list: The total profit or loss from the stock transactions.
    """

    if transaction["operation"] == "buy" and weight_average_cost >= 0:
        weight_average_cost, current_quantity = define_weight_average_cost(transaction, weight_average_cost, current_quantity)
    elif transaction["operation"] == "sell":
        if transaction["unit-cost"] < weight_average_cost and current_quantity > transaction["quantity"]:
            transaction["profit"] = 0
            transaction["loss"] = calculate_loss(transaction, weight_average_cost)
            cumulative_loss = transaction["loss"]
        else:
            transaction["profit"], cumulative_loss = calculate_profit(transaction, weight_average_cost, cumulative_loss)
            transaction["loss"] = 0
        current_quantity = current_quantity - transaction["quantity"]

    return transaction, cumulative_loss, current_quantity, weight_average_cost


def calculate_profit(transaction, weight_average_cost, cumulative_loss):
    """
    Calculate the total profit from a list of stock transactions.

    Parameters:
    - stocks_transactions (list of dict): List of stock transaction dictionaries, where each dictionary contains
      information about a single transaction, including "unit-cost", "quantity", and "weight_average_cost".

    Returns:
    - float: Total profit calculated from the provided list of stock transactions.
    """

    total_operation = transaction["unit-cost"] * transaction["quantity"]
    total_operation_wac = transaction["quantity"] * weight_average_cost

    profit = abs(total_operation - total_operation_wac)

    if cumulative_loss > 0:
        cumulative_loss = abs(profit - cumulative_loss)
        if cumulative_loss == 0 or cumulative_loss >= profit:
            profit = cumulative_loss
        else:
            profit = cumulative_loss
            cumulative_loss = 0
    return profit, cumulative_loss


def calculate_loss(transaction, weight_average_cost):
    """
    Calculate the total loss from a list of stock transactions based on the provided profit.

    Parameters:
    - stocks_transactions (list of dict): List of stock transaction dictionaries, where each dictionary contains
      information about a single transaction, including "operation", "unit-cost", and "weight_average_cost".
    - profit (float): The total profit obtained from the stock transactions.

    Returns:
    - float: Total loss calculated based on the provided profit and stock transactions.
    """

    loss = 0

    if transaction["operation"] == "sell" and transaction["unit-cost"] <= weight_average_cost:
        total_operation = transaction["unit-cost"] * transaction["quantity"]
        total_weight_average_cost = transaction["quantity"] * weight_average_cost
        loss = abs(total_operation - total_weight_average_cost)

    return loss



