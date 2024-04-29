
from src.calculations.calculate_profit_loss import calculate_profit_loss
from src.calculations.calculate_taxes import calculate_taxes
from src.utils.utils import input_data_format, output_data_format


class CapitalGain:
    def __init__(self, stocks_transactions: str):
        self.stocks_operations = stocks_transactions

    def capital_gain(self):
        """
        Calculate taxes based on the given stock transaction.

        Parameters:
        - transaction (dict): Dictionary representing a list stock transactions.

        Returns:
        - dict: Dictionary containing tax information for the transactions.

        Example:
        - transaction = {'operation': 'sell', 'unit-cost': 15.00, 'quantity': 50, 'profit': 1000.00, 'loss': 0.00}
        - calculate_taxes(transaction) : {'tax': 200.0}
        """
        tax_output = ''
        current_quantity = 0
        weight_average_cost = 0
        cumulative_loss = 0

        stocks_transactions_list = input_data_format(self.stocks_operations)

        for stock_operation in stocks_transactions_list:

            taxes_calculated = []
            for operation in stock_operation:
                profit_or_loss_stocks_list, cumulative_loss, current_quantity, weight_average_cost = calculate_profit_loss(
                    operation, weight_average_cost, current_quantity, cumulative_loss)
                taxes = calculate_taxes(operation, cumulative_loss)
                taxes_calculated.append(taxes)
            tax_output += output_data_format(taxes_calculated)

        return tax_output


