from pydantic import BaseModel, Field
from typing import Optional
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,                 # '...' means this field is required
        min_length=3,        # minimum length of the string
        max_length=50,       # maximum length of the string
        description="Employee Name",
        example="Ritik Sharma"  # Pydantic uses 'example' (singular) for examples
    )
    department: Optional[str] = 'General'  # Optional field with default value 'General'
    salary: float = Field(
        ...,
        ge=10000,            # salary must be >= 10000
        description="Monthly salary"
    )

class User(BaseModel):
    email: str = Field(
        ...,
        regex=r'^[\w\.-]+@[\w\.-]+\.\w+$',  # Simple regex for validating email format
        description="User email address"
    )
    phone: str = Field(
        ...,
        min_length=10,       # phone number must be exactly 10 characters
        max_length=10,
        description="Phone number with 10 digits"
    )
    age: int = Field(
        ...,
        ge=18,               # age >= 18
        le=60,               # age <= 60
        description="Age in years"
    )
    discount: float = Field(
        ...,
        ge=0,                # discount >= 0%
        le=100,              # discount <= 100%
        description="Discount percentage"
    )
