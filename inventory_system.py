import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item with a given quantity to the stock.
    """
    if logs is None:
        logs = []

    if not isinstance(item, str):
        raise TypeError("Item name must be a string")

    if not isinstance(qty, int):
        raise TypeError("Quantity must be an integer")

    if not item:
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove a quantity of an item from stock.
    """
    if not isinstance(item, str) or not isinstance(qty, int):
        return

    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    """
    Return the quantity of an item, or zero if missing.
    """
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """
    Load inventory data from a JSON file.
    """
    global stock_data
    with open(file_path, "r", encoding="utf-8") as f:
        stock_data = json.load(f)


def save_data(file_path="inventory.json"):
    """
    Save current inventory to a JSON file.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data():
    """
    Print all inventory items.
    """
    print("Items Report")
    for item_name, qty in stock_data.items():
        print(f"{item_name} -> {qty}")


def check_low_items(threshold=5):
    """
    Return list of items with quantity below a threshold.
    """
    result = []
    for item_name, qty in stock_data.items():
        if qty < threshold:
            result.append(item_name)
    return result


def main():
    """
    Demo execution of the inventory system.
    """
    add_item("apple", 10)
    add_item("banana", -2)
    remove_item("apple", 3)
    remove_item("orange", 1)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())

    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
