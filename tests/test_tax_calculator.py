from io import StringIO
from unittest.mock import patch
import os
import sys

# get the project path dynamically to avoid hardcoded path
project_path = os.path.abspath(os.path.join(''))

# check the path is not already in sys.path, to avoid duplicates
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from src.tax_calculator.calculator_tax import *

def test_capital_gains_case_01():

    result_expected = '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00}]'
    # Mocking stdin
    with patch('sys.stdin', StringIO('[{"operation":"buy", "unit-cost":10.00, "quantity": 100}, '
                                     '{"operation":"sell", "unit-cost":15.00, "quantity": 50}, '
                                     '{"operation":"sell", "unit-cost":15.00, "quantity": 50}]\n')) as stdin, \
            patch('sys.stdout', new_callable=StringIO) as stdout:

        list_stocks_operations = stdin.read()
        taxes = TaxCalculator(list_stocks_operations).capital_gain()

        assert taxes == result_expected


def test_capital_gains_case_02():

    result_expected = '[{"tax": 0.00},{"tax": 10000.00},{"tax": 0.00}]'
    # Mocking stdin
    with patch('sys.stdin', StringIO('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, {"operation":"sell", "unit-cost":20.00, "quantity": 5000}, {"operation":"sell", "unit-cost":5.00, "quantity": 5000}]\n')) as stdin, \
            patch('sys.stdout', new_callable=StringIO) as stdout:

        list_stocks_operations = stdin.read()
        taxes = TaxCalculator(list_stocks_operations).capital_gain()

        assert taxes == result_expected


def test_capital_gain_case_01_and_02():

    result_expected = '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00}][{"tax": 0.00},{"tax": 10000.00},{"tax": 0.00}]'
    # Mocking stdin
    with patch('sys.stdin', StringIO('[{"operation":"buy", "unit-cost":10.00, "quantity": 100},'
                                     ' {"operation":"sell", "unit-cost":15.00, "quantity": 50},'
                                     '{"operation":"sell", "unit-cost":15.00, "quantity": 50}]\n'
                                     '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, '
                                     '{"operation":"sell", "unit-cost":20.00, "quantity": 5000}, '
                                     '{"operation":"sell", "unit-cost":5.00, "quantity": 5000}]\n')) as stdin, \
            patch('sys.stdout', new_callable=StringIO) as stdout:

        list_stocks_operations = stdin.read()
        taxes = TaxCalculator(list_stocks_operations).capital_gain()
        assert taxes == result_expected


def test_capital_gain_case_03():

    result_expected = '[{"tax": 0.00},{"tax": 0.00},{"tax": 1000.00}]'
    # Mocking stdin
    with patch('sys.stdin', StringIO('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, '
                                     '{"operation":"sell", "unit-cost":5.00, "quantity": 5000}, '
                                     '{"operation":"sell", "unit-cost":20.00, "quantity": 3000}]\n')) as stdin, \
            patch('sys.stdout', new_callable=StringIO) as stdout:

        list_stocks_operations = stdin.read()
        taxes = TaxCalculator(list_stocks_operations).capital_gain()
        assert taxes == result_expected


def test_capital_gain_case_04():

    result_expected = '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00}]'
    # Mocking stdin
    with patch('sys.stdin', StringIO('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, '
                                     '{"operation":"buy", "unit-cost":25.00, "quantity": 5000}, '
                                     '{"operation":"sell", "unit-cost":15.00, "quantity": 10000}]\n')) as stdin, \
            patch('sys.stdout', new_callable=StringIO) as stdout:

        list_stocks_operations = stdin.read()
        taxes = TaxCalculator(list_stocks_operations).capital_gain()
        assert taxes == result_expected


def test_capital_gain_case_05():

    result_expected = '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 10000.00}]'
    # Mocking stdin
    with patch('sys.stdin', StringIO('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, '
                                     '{"operation":"buy", "unit-cost":25.00, "quantity": 5000}, '
                                     '{"operation":"sell", "unit-cost":15.00, "quantity": 10000}, '
                                     '{"operation":"sell", "unit-cost":25.00, "quantity": 5000}]\n')) as stdin, \
            patch('sys.stdout', new_callable=StringIO) as stdout:

        list_stocks_operations = stdin.read()
        taxes = TaxCalculator(list_stocks_operations).capital_gain()
        assert taxes == result_expected


def test_capital_gain_case_06():

    result_expected = '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 3000.00}]'
    # Mocking stdin
    with patch('sys.stdin', StringIO('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, '
                                     '{"operation":"sell", "unit-cost":2.00, "quantity": 5000}, '
                                     '{"operation":"sell", "unit-cost":20.00, "quantity": 2000}, '
                                     '{"operation":"sell", "unit-cost":20.00, "quantity": 2000}, '
                                     '{"operation":"sell", "unit-cost":25.00, "quantity": 1000}]\n')) as stdin, \
            patch('sys.stdout', new_callable=StringIO) as stdout:

        list_stocks_operations = stdin.read()
        taxes = TaxCalculator(list_stocks_operations).capital_gain()
        assert taxes == result_expected


def test_capital_gain_case_07():

    result_expected = '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 3000.00},' \
                      '{"tax": 0.00},{"tax": 0.00},{"tax": 3700.00},{"tax": 0.00}]'
    # Mocking stdin
    with patch('sys.stdin', StringIO('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, '
                                     '{"operation":"sell", "unit-cost":2.00, "quantity": 5000}, '
                                     '{"operation":"sell", "unit-cost":20.00, "quantity": 2000}, '
                                     '{"operation":"sell", "unit-cost":20.00, "quantity": 2000}, '
                                     '{"operation":"sell", "unit-cost":25.00, "quantity": 1000}, '
                                     '{"operation":"buy", "unit-cost":20.00, "quantity": 10000}, '
                                     '{"operation":"sell", "unit-cost":15.00, "quantity": 5000}, '
                                     '{"operation":"sell", "unit-cost":30.00, "quantity": 4350}, '
                                     '{"operation":"sell", "unit-cost":30.00, "quantity": 650}]\n')) as stdin, \
            patch('sys.stdout', new_callable=StringIO) as stdout:

        list_stocks_operations = stdin.read()
        taxes = TaxCalculator(list_stocks_operations).capital_gain()
        assert taxes == result_expected
