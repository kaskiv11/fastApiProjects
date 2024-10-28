from datetime import datetime

from pydantic import BaseModel, field_validator


class MyModel(BaseModel):
    expiration_date: datetime

    @field_validator("expiration_date")
    def validate_expiration_date(cls, value):
        if value < datetime.now():
            raise ValueError("Expiration date must be in the future")
        return value


def is_even(n):
    return n % 2 == 0


def find_element(my_list, element):
    return element in my_list