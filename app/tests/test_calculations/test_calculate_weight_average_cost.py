from src.calculations.calculate_weight_average_cost import calculate_new_weight_average_cost, define_weight_average_cost


def test_calculate_new_weight_average_cost():
    transaction = {"operation": "buy", "unit-cost": 10.0, "quantity": 1000}
    weight_average_cost = 20.0
    current_quantity = 200
    result = calculate_new_weight_average_cost(transaction, weight_average_cost, current_quantity)
    assert round(result, 2) == 11.67


def test_define_weight_average_cost():
    operation = {"operation": "buy", "unit-cost": 10.0, "quantity": 1000}
    weight_average_cost = 20.0
    current_quantity = 200
    result_weight_average_cost, result_current_quantity = define_weight_average_cost(operation, weight_average_cost, current_quantity)
    assert round(result_weight_average_cost, 2) ==  11.67
    assert result_current_quantity == 200


