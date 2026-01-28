from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username: str

    @field_validator('username')  # Validator for the 'username' field only
    def username_length(cls, v):  # cls = class, v = value of username
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')  # Runs after model is initialized, validates entire model
    def password_match(cls, values):
        # values is a dict with all fields after initial validation
        if values.password != values.confirm_password:
            raise ValueError("Passwords do not match")
        return values
