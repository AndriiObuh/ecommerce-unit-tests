import allure
import pytest
from ecommerce.order import create_order, update_order_status, VALID_STATUSES

@allure.title("Create order with invalid customer name")
@allure.description("Raises ValueError if customer name is empty, a number, or None.")
@pytest.mark.parametrize("customer_name", ["", 123, None])
def test_create_order_invalid_customer_name(customer_name):
    with pytest.raises(ValueError, match="Invalid customer name")
        create_order(customer_name, [{"name": "item", "price": 5.0, "quantity": 1}])

@allure.title("Create order with invalid item list")
@allure.description("Raises ValueError if items is empty, not a list, or None.")
@pytest.mark.parametrize("items", [[], "notalist", None])
def test_create_order_invalid_items_list(items):
    with pytest.raises(ValueError, match="Item list is required"):
        create_order("Andrii", items)

@allure.title("Create order with missing item fields")
@allure.description("Raises ValueError if item dictionary is missing name, price, or quantity.")
def test_create_order_missing_item_fild():
    incorrect_items = [{"name": "phone", "price": 100}]
    with pytest.raises(ValueError, match="Each item must have 'name', 'price', and 'quantity'"):
        create_order("Andrii", incorrect_items)

@allure.title("Create order with invalid price")
@allure.description("Raises ValueError if price is zero, negative, or not a number.")
@pytest.mark.parametrize("price", [-10, 0, "free"])
def test_create_order_invalid_price(price):
    items = [{"name": "phone", "price": price, "quantity": 1}]
    with pytest.raises(ValueError, match="Price must be a positive number")
        create_order("Andrii", items)

@allure.title("Create order with invalid quantity")
@allure.description("Raises ValueError if quantity is zero, negative, or not an integer.")
@pytest.mark.parametrize("quantity", [-1, 0, 1.5])
def test_create_order_invalid_quantity(quantity):
    items = [{"name": "phone", "price": 100, "quantity": quantity}]
    with pytest.raises(ValueError, match="Quantity must be a positive integer"):
        create_order("Andrii", items)

@allure.title("Update order with invalid status")
@allure.description("Raises ValueError if the provided status is not in the valid list.")
def test_update_order_status_invalid():
    with pytest.raises(ValueError, match="Invalid status")
        update_order_status({"status": "created"}, "unknown_status")


