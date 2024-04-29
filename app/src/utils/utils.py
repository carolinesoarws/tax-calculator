
import json
import re


def input_data_format(stocks_transactions_raw_input):
    """
    Parse the raw input string containing stock transactions and return a list of transactions.

    Parameters:
    - stocks_transactions_raw_input (str): Raw input string containing stock transactions.

    Returns:
    - list: List of dictionaries representing individual stock transactions.

    """
    transactions = []
    if stocks_transactions_raw_input != '':

        if stocks_transactions_raw_input.endswith('\n'):
            transactions_raw = stocks_transactions_raw_input.strip().split('\n')

            for transaction_raw in transactions_raw:
                transaction_split = re.split(r'(?<=\]) (?=\[)', transaction_raw)
                for split in transaction_split:
                    transaction = json.loads(split)
                    transactions.append(transaction)
        else:
            if len(transactions) > 1:
                transactions = re.split(r'(?<=\]) (?=\[)', stocks_transactions_raw_input)
                for transaction in transactions:
                    transaction = json.loads(transaction)
                    transactions.append(transaction)
            else:
                transactions = json.loads(stocks_transactions_raw_input)
    return transactions


def output_data_format(tax_list):
    """
    Format tax information into a JSON-like string.

    Parameters:
    - tax_list (list): List of dictionaries containing tax information.

    Returns:
    - str: Formatted string containing tax information.

    """

    formatted_strings = [f'{{"tax": {d["tax"]:.2f}}}' for d in tax_list]
    formatted_output = '[' + ','.join(formatted_strings) + ']'

    return formatted_output
