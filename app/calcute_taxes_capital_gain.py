import sys

from src.capital_gains.capital_gain import CapitalGain

if __name__ == '__main__':
    """
        Main entry point of the Capital Gain Calculator program.

        This script reads stock transactions from standard input, initializes the CapitalGain class with the transactions,
        calculates taxes using the CapitalGain class, and prints the calculated taxes.

        Usage:
        - Input: Stock transactions provided through standard input (stdin)
        - Output: Calculated taxes for the stock transactions

        """
    stocks_transactions_input = ""
    try:

        for line in sys.stdin:
            stocks_transactions_input = line

            print("")
            print("******************************************************")
            print(" Starting Stocks Tax Calculator ")
            print("******************************************************")
            print("")
            print("# Stocks transactions: ", stocks_transactions_input)

            taxes_capital_gain = CapitalGain(str(stocks_transactions_input)).capital_gain()

            print("# Tax stocks transactions: ",taxes_capital_gain)

            print("")
            print("******************************************************")
            print(" Finising Stock Tax Calculator ")
            print("******************************************************")
            print("")
            break
    except Exception as e:
        print("An error occur:", e)
