# pytest runs every function whose name starts with test_, in every file whose name starts with test_.
# With the virtual environment activated, run it from this folder: python3 -m pytest
from orders import add_purchase, get_total

def test_get_total_multiplies_each_quantity_by_its_price():
    add_purchase("coffee", 2)
    add_purchase("bagel", 1)
    assert get_total() == 9.25
