from pydantic import BaseModel
from typing import Optional, List, Union


# ---------- BASIC NESTED MODELS ----------

class Address(BaseModel):
    street: str        # Street name
    city: str          # City name
    postal_code: str   # Postal / ZIP code

class Company(BaseModel):
    name: str
    address: Optional[Address] = None   # Company may or may not have an address

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None   # Employee may or may not belong to a company


# ---------- UNION / POLYMORPHIC CONTENT MODELS ----------

class TextContent(BaseModel):
    type: str = "text"   # Discriminator field
    Content: str        # Text section content

class ImageContent(BaseModel):
    type: str = "Image" # Discriminator field
    url: str            # Image URL
    alt_text: str       # Image description

class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]
    # Sections can be either text OR image blocks


# ---------- DEEPLY NESTED HIERARCHY MODELS ----------

class Country(BaseModel):
    name: str
    code: str           # Country code (e.g., IN, US)

class State(BaseModel):
    name: str
    country: Country    # Each state belongs to a country

class City(BaseModel):
    name: str
    state: State        # Each city belongs to a state

class Address(BaseModel):
    name: str           # Address label or location name
    city: City
    postal_code: str

class Organization(BaseModel):
    name: str
    heaad_quater: Address   # ⚠ Typo preserved as-is (should be 'head_quarter')
    branches: List[Address] = []   # Multiple branch addresses
