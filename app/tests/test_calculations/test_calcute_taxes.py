from src.calculations.calculate_taxes import calculate_taxes


def test_buy_operation():
    transaction = {"operation": "buy", "unit-cost": 10.0, "quantity": 100, "profit": 0.0, "loss": 0.0}
    cumulative_loss = 0.0
    result = calculate_taxes(transaction, cumulative_loss)
    assert result["tax"] == 0.0


def test_sell_operation_no_tax():
    transaction = {"operation": "sell", "unit-cost": 10.0, "quantity": 100, "profit": 2000.0, "loss": 0.0}
    cumulative_loss = 0.0
    result = calculate_taxes(transaction, cumulative_loss)
    assert result["tax"] == 0.0


def test_sell_operation_with_tax():
    transaction = {"operation": "sell", "unit-cost": 10.0, "quantity": 10000, "profit": 2000.0, "loss": 0.0}
    cumulative_loss = 1000.0
    result = calculate_taxes(transaction, cumulative_loss)
    assert result["tax"] == 200.0
