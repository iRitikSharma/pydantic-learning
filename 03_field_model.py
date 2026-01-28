from pydantic import BaseModel
from typing import List, Dict, Optional

# Model representing a shopping cart
class Cart(BaseModel):
    user_id: int                # ID of the user owning the cart
    item: List[str]             # List of item names in the cart
    quantities: Dict[str, int]  # Mapping of item names to their quantities

# Model representing a blog post
class BlogPost(BaseModel):
    title: str                  # Title of the blog post
    content: str                # Main content of the post
    image_url: Optional[str] = None  # Optional image URL

# Sample cart data in dictionary format
Cart_data = {
    'user_id': 123,
    'item': ['Laptop', 'mouse', 'keyboard'],
    'quantities': {'Laptop': 2, 'mouse': 1, 'keyboard': 3}
}

# Create a Cart object by unpacking the dict
cart = Cart(**Cart_data)
print(cart)
