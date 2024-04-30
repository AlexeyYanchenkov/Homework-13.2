from src.category import Category
from src.products import Product

category = Category('Смартфоны', "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни", [])
samsung = Product.create_product({
        "name": "Samsung Galaxy S24 Ultra",
        "description": "256GB, Черный титан, 200MP камера",
        "price": 146990.0,
        "quantity": 15
      })
category.add_product(samsung)


print(samsung)
print(category.products)
