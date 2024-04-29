from src.calculations.calculate_profit_loss import calculate_profit, calculate_loss, calculate_profit_loss

def test_calculate_profit_loss_buy_operation():
    transaction = {"operation": "buy", "unit-cost": 10.0, "quantity": 100}
    weight_average_cost = 0.0
    current_quantity = 0
    cumulative_loss = 0.0
    result_transaction, result_cumulative_loss, result_current_quantity, result_weight_average_cost = calculate_profit_loss(transaction, weight_average_cost, current_quantity, cumulative_loss)
    assert result_weight_average_cost == 10.0
    assert result_current_quantity == 100
    assert result_cumulative_loss == 0.0


def test_calculate_profit_loss_sell_operation_profit():
    transaction = {"operation": "sell", "unit-cost": 15.0, "quantity": 50}
    weight_average_cost = 10.0
    current_quantity = 100
    cumulative_loss = 0.0
    result_transaction, result_cumulative_loss, result_current_quantity, result_weight_average_cost = calculate_profit_loss(transaction, weight_average_cost, current_quantity, cumulative_loss)
    assert result_transaction["profit"] == 250.0
    assert result_cumulative_loss == 0.0
    assert result_current_quantity == 50
    assert result_weight_average_cost == 10.0


def test_calculate_profit_loss_sell_operation_loss():
    transaction = {"operation": "sell", "unit-cost": 5.0, "quantity": 150}
    weight_average_cost = 10.0
    current_quantity = 100
    cumulative_loss = 0.0
    result_transaction, result_cumulative_loss, result_current_quantity, result_weight_average_cost = calculate_profit_loss(transaction, weight_average_cost, current_quantity, cumulative_loss)
    assert result_transaction["loss"] == 0
    assert result_cumulative_loss == 0
    assert result_current_quantity == -50
    assert result_weight_average_cost == 10.0


def test_calculate_profit():
    transaction = {"unit-cost": 15.0, "quantity": 50}
    weight_average_cost = 10.0
    cumulative_loss = 0.0
    result_profit, result_cumulative_loss = calculate_profit(transaction, weight_average_cost, cumulative_loss)
    assert result_profit == 250.0
    assert result_cumulative_loss == 0.0


def test_calculate_loss():
    transaction = {"operation": "sell", "unit-cost": 5.0, "quantity": 150}
    weight_average_cost = 10.0
    result_loss = calculate_loss(transaction, weight_average_cost)
    assert result_loss == 750.0
