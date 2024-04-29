

def calculate_taxes(transaction, cumulative_loss):
    """
    Calculates taxes based on the transaction details.

    Args:
        transaction (dict): A dictionary representing the transaction with keys:
                            - "operation": String representing the type of operation ("buy" or "sell").
                            - "unit-cost": Float representing the unit cost of the transaction.
                            - "quantity": Integer representing the quantity of stocks involved in the transaction.
                            - "profit": Float representing the profit of the transaction.
                            - "loss": Float representing the loss of the transaction.

    Returns:
        dict: A dictionary containing the calculated taxes.
    """

    taxes = {}
    if transaction["operation"] == "buy":
        taxes["tax"] = round(float(0), 2)
    elif transaction["operation"] == "sell":
        total_transaction = transaction["unit-cost"] * transaction["quantity"]
        if total_transaction <= 20000 or total_transaction <= transaction["profit"] or transaction["loss"] > 0:
            taxes["tax"] = round(float(0), 2)
        else:
            if cumulative_loss > 0:
                profit_updated = abs(transaction["profit"] - cumulative_loss)
                tax = (profit_updated * 20) / 100
            else:
                tax = (transaction["profit"] * 20) / 100
            taxes["tax"] = round(float(tax), 2)

    return taxes

