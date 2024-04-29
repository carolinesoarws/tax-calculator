from src.utils.utils import input_data_format, output_data_format


def test_input_data_format_multiple_transactions():
    stocks_transactions_raw_input = '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, ' \
                                    '{"operation":"buy", "unit-cost":25.00, "quantity": 5000}, ' \
                                     '{"operation":"sell", "unit-cost":15.00, "quantity": 10000}, ' \
                                     '{"operation":"sell", "unit-cost":25.00, "quantity": 5000}]\n'
    expected_transactions = [[{'operation': 'buy', 'quantity': 10000, 'unit-cost': 10.0},
                              {'operation': 'buy', 'quantity': 5000, 'unit-cost': 25.0},
                              {'operation': 'sell', 'quantity': 10000, 'unit-cost': 15.0},
                              {'operation': 'sell', 'quantity': 5000, 'unit-cost': 25.0}]]
    result_transactions = input_data_format(stocks_transactions_raw_input)
    assert result_transactions == expected_transactions


def test_input_data_format_single_transaction():
    stocks_transactions_raw_input = '[{"operation": "buy", "unit-cost": 10.0, "quantity": 100}]'
    expected_transactions = [{"operation": "buy", "unit-cost": 10.0, "quantity": 100}]
    result_transactions = input_data_format(stocks_transactions_raw_input)
    assert result_transactions == expected_transactions


def test_input_data_format_no_transactions():
    stocks_transactions_raw_input = ''
    expected_transactions = []
    result_transactions = input_data_format(stocks_transactions_raw_input)
    assert result_transactions == expected_transactions


def test_output_data_format_single_tax():
    tax_list = [{"tax": 200.0}]
    expected_output = '[{"tax": 200.00}]'
    result_output = output_data_format(tax_list)
    assert result_output == expected_output


def test_output_data_format_multiple_taxes():
    tax_list = [{"tax": 200.0}, {"tax": 300.0}, {"tax": 150.0}]
    expected_output = '[{"tax": 200.00},{"tax": 300.00},{"tax": 150.00}]'
    result_output = output_data_format(tax_list)
    assert result_output == expected_output


def test_output_data_format_no_taxes():
    tax_list = []
    expected_output = '[]'
    result_output = output_data_format(tax_list)
    assert result_output == expected_output