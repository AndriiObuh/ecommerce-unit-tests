import allure
import pytest
from ecommerce.order import create_order, update_order_status, VALID_STATUSES


@allure.title("Create order with valid data")
@allure.description("Checks that name, total, items, and status are set correctly.")
@pytest.mark.parametrize("customer_name, items, expected_total", [
    ("Andrii", [{"name": "phone", "price": 99.0, "quantity": 2}], 198.0),
    ("Viktoria", [{"name": "laptop", "price": 200.0, "quantity": 1}], 200.0)
])
def test_create_order_valid_data(customer_name, items, expected_total):
    order = create_order(customer_name, items)
    assert order["customer"] == customer_name
    assert order["items"] == items
    assert order["status"] == "created"
    assert order["total"] == expected_total


@allure.title("Update order status with valid values")
@allure.description("Checks that name, total, items, and status are set correctly.")
@pytest.mark.parametrize("new_status", VALID_STATUSES)
def test_update_order_status_valid(new_status):
    order = {"status": "created"}
    updated = update_order_status(order, new_status)
    assert updated["status"] == new_status
