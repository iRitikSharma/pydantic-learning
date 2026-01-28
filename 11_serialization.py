from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str       # Street name as a string
    city: str         # City name as a string
    zip_code: str     # Postal/Zip code as a string

class User(BaseModel):
    id: int                   # User ID as an integer
    name: str                 # User name as a string
    email: str                # User email as a string
    is_active: bool = True    # Whether user is active, defaults to True if not provided
    created_at: datetime      # DateTime object representing user creation time
    address: Address          # Nested Address model for user’s address
    tags: List[str] = []      # List of tags (strings), defaults to empty list

    # Custom model configuration:
    model_config = ConfigDict(
        # Customize how datetime objects are converted to JSON strings
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
        # This formats datetime as 'day-month-year hour:minute:second'
    )

# -----------------------------
# Pydantic Useful Functions:
# -----------------------------

# 1. model_dump():
#    - Use this when you want a Python dict representation of your model.
#    - Includes nested models as nested dicts.
#    - Useful for internal data manipulation or passing data to other functions.
#
#    Example:
#    user_dict = user.model_dump()
#
# 2. model_dump_json():
#    - Use this to get a JSON string representation of your model.
#    - Respects any custom json_encoders you define in model_config.
#    - Ideal for API responses, logging, or storing JSON.
#
#    Example:
#    user_json = user.model_dump_json()
#
# 3. Validation and Type Enforcement:
#    - Pydantic automatically validates input types on model creation.
#    - Raises clear errors if data is missing or invalid.
#    - Helps catch bugs early and ensures data integrity.
#
# 4. Nested Models:
#    - Use nested models (like Address inside User) to structure complex data.
#    - Automatically validates nested fields.
#
# 5. Default Values:
#    - You can specify defaults (like is_active=True) so callers don't need to provide every field.
#
# -----------------------------

# Creating an instance of User with all required and optional data
user = User(
    id=1,
    name="Ritik",
    email="ritik@gmail.com",   # Fixed typo (comma to dot)
    created_at=datetime(2024, 3, 15, 14, 30),  # March 15, 2024 at 14:30
    address=Address(
        street='something',
        city='Delhi',
        zip_code='00988'
    ),
    is_active=False,            # Explicitly setting is_active to False
    tags=["premium", "Subscriber"]  # List of tags assigned to user
)

print(user)  # Prints the User model instance with all fields

print("=" * 60)

python_dict = user.model_dump()  # Converts model to a Python dict (including nested models)
print(python_dict)               # Print the dict representation

print("=" * 60)

json_str = user.model_dump_json()  # Converts model to a JSON string with custom datetime formatting
print(json_str)                    # Print JSON string

print("=" * 60)
