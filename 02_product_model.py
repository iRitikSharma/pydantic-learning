from pydantic import BaseModel

# Define a Product model with type annotations for automatic validation
class Product(BaseModel):
    id: int              # Product ID (required)
    name: str            # Product name (required)
    price: float         # Product price (required)
    in_stock: bool = True  # Whether product is in stock (default True)

# Creating product with all fields specified
product_one = Product(id=1, name='Laptop', price=999.99, in_stock=True)
print(product_one)

# Creating product without specifying 'in_stock', uses default True
product_two = Product(id=2, name='Mouse', price=24.99)
print(product_two)

# This will raise an error because required fields 'id' and 'price' are missing
try:
    product_three = Product(name='Keyboard')
except Exception as e:
    print(f"Error creating product_three: {e}")
