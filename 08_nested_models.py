from typing import List, Optional
from pydantic import BaseModel

# Address model to store address-related data
class Address(BaseModel):
    street: str        # Street name
    city: str          # City name
    postal_code: str   # Postal / ZIP code

# User model with a nested Address model
class User(BaseModel):
    id: int            # Unique user ID
    name: str          # User name
    address: Address   # Nested Address object

# Dictionary-style input (commonly comes from JSON / API request)
user_data = {
    'id': 1,
    'name': 'Ritik',
    'address': {
        'street': '321 something',
        'city': 'New York',
        'postal_code': '1012'
    }
}

# ** unpacks dictionary keys and values into the User model
# Pydantic automatically converts 'address' dict into Address model
user = User(**user_data)

# Prints validated and structured data
print(user)
