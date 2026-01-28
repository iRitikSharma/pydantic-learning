from pydantic import BaseModel, Field, computed_field

class Product(BaseModel):
    price: float         # Price per unit
    quantity: int        # Number of units purchased

    @computed_field       # Marks this method as a computed property
    def total_price(self) -> float:
        # Automatically calculates total price (price * quantity)
        return self.price * self.quantity

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(
        ...,              # Required field
        ge=1               # Minimum value is 1 (can't book zero or negative nights)
    )
    rate_per_night: float  # Cost per night for the room

    @computed_field
    def total_amount(self) -> float:
        # Automatically calculates total cost for the booking
        return self.nights * self.rate_per_night

# Creating an instance of Booking with required data
booking = Booking(
    user_id=123,
    room_id=23,
    nights=7,
    rate_per_night=999
)

# Accessing computed field like a regular attribute
print(booking.total_amount)  # Output: 6993 (7 * 999)

# model_dump() converts the entire model to a dict, including computed fields
print(booking.model_dump())
# Output:
# {
#   'user_id': 123,
#   'room_id': 23,
#   'nights': 7,
#   'rate_per_night': 999.0,
#   'total_amount': 6993.0    # Notice this is included automatically!
# }
