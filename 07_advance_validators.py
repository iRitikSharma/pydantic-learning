from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_name')
    def names_must_be_capitalized(cls, v):
        # Check if each name is capitalized (e.g., "John", not "john")
        if not v.istitle():
            raise ValueError("Names must be capitalized")
        return v

class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, v):
        # Convert email to lowercase and strip whitespace
        return v.lower().strip()

class Product(BaseModel):
    price: float   # Changed from str to float for better type safety

    @field_validator('price', mode='before')
    def parse_price(cls, v):
        # Converts string price like "$4.44" to float before validation
        if isinstance(v, str):
            return float(v.replace('$', '').replace(',', ''))
        return v

class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime   # Fixed field name typo: end_time -> end_date

    @model_validator(mode='after')
    def validate_date_range(cls, values):
        # Ensure start_date is before end_date
        if values.start_date >= values.end_date:
            raise ValueError("end_date must be after start_date")
        return values
