import pytest

from src.products import Product


@pytest.fixture
def product1():
    return Product("Iphone 15", "512GB, Black, 48MP камера", 114990.0, 10)


@pytest.fixture
def product2():
    return Product("Samsung Galaxy S24 Ultra", "256GB, Черный титан, 200MP камера", 146990.0, 15)


def test_product_init(product2):
    assert product2.name == "Samsung Galaxy S24 Ultra"
    assert product2.description == "256GB, Черный титан, 200MP камера"
    assert product2.price == 146990.0
    assert product2.quantity == 15


def test_create_product(product1):
    product1.price = 0
    assert product1.price == 114990.0
    product1.price = 12000.0
    assert product1.price == 12000.0
