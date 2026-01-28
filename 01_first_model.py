print("Start of Pydantic Journey") 

# 🔹 What is Pydantic?
# Pydantic is a Python library that uses type hints to:
# - Validate data automatically
# - Convert types if possible (e.g., str to int)
# - Raise clear errors if data is invalid

from pydantic import BaseModel

class User(BaseModel):
    id: int           # User ID must be an integer
    name: str         # User name must be a string
    is_active: bool   # User status must be boolean (True or False)

# Example input data where 'is_active' is an integer (25)
input_data = {
    'id': 101,
    'name': 'Ritik',
    'is_active': 25   # Note: This is NOT a boolean, but an int
}

# Pydantic will try to convert this automatically:
# bool(25) is True in Python, so this will pass validation
user = User(**input_data)

# Print the parsed & validated User object
print(user)
