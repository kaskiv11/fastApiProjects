from datetime import datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field, field_validator, validator


class UserType(Enum):
    ADMIN = "admin"
    USER = "user"


print(UserType.ADMIN.USER.name)
print(UserType.ADMIN.USER.value)


class User(BaseModel):
    name: str
    email: EmailStr
    user_type: UserType = UserType.USER


user = User(name="Jhon", email="email@gmail.com")
print(user)



class EventModel(BaseModel):
    name: str= Field(..., example="Tech Conference")
    description: Optional[str] = Field(None, example="A conference about technology")
    start_datetime: datetime = Field(..., example="2024-10-07T09:00:00Z")
    emails: List[str] = Field(..., example=["email@gmail.com"])

    @validator('emails', each_item=True)
    def validate_email(cls, v):
        return v

    class Config:
        min_anystr_length = 1
        max_anystr_length = 255
        error_msg_templates = {
            'value_error.missing': 'field required',
            'value_error.anystr:min_length': 'ensure this value has at least {limit_value} characters',
            'value_error.anystr:max_length': 'ensure this value has no more then {limit_value} characters',
            'value_error.datetime': 'incorrect datetime format, use YYYY-MM-DDTHH:MM:SS format'
        }


try:
    event = EventModel(
        name="Tech Conference",
        description="",
        start_datetime="2024-10-07T09:00:00Z",
        emails=["email@gmail.com", 'incorrect email format']
    )
except Exception as e:
    print("Exception: ", e)
print(event)