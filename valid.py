from datetime import datetime
from typing import Optional, List

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, constr, EmailStr, validator, conint, ValidationError, conlist
#from flask_sqlalchemy import SQLAlchemy

app = FastAPI()


class Address(BaseModel):
    street: str
    city: str
    postal_code: constr(min_length=5, max_length=10)


class User(BaseModel):
    id: int
    name: constr(min_length=3, max_length=20)
    email: EmailStr
    age: conint(ge=10, le=99)
    salary: Optional[conint(ge=0)] = None
    is_employee: bool
    address: Address
    hobbies: List[str]
    created_at = Optional[datetime]

    @validator('salary')
    def check_employee_salary(cls, v, values):
        if values['is_employee'] and v is None:
            raise ValueError("Employee has to salary")
        return v

    @validator('hobbies')
    def check_unique_hobbies(cls, v):
        if len(v) != len(set(v)):
            raise ValueError("Hobbies must have unique")
        return v


@app.post("/users")
async def create_user(user:User):
    if user.age < 10:
        raise HTTPException(status_code=400, detail="Age must be at least 10")
    if len(user.hobbies) < 1:
        raise HTTPException(status_code=400, detail="User must have at least one hobbie")
    return {"message": "User created", "data": user}


class Item(BaseModel):
    name: str
    description: str
    price: float


class ItemList(BaseModel):
    items: List[Item]


data_to_validate = {
    "items": [
        {'name': "Apple", "description": "Fruit", "price": 2.5},
        {'name': "Orange", "description": "Fruit", "price": 3.2},
        {'name': "Orange", "description": "Fruit", "price": "unknown"}
    ]
}

try:
    validated_data = ItemList(**data_to_validate)
    print(validated_data)
except ValidationError as e:
    print("Error validation: ")
    print(e.json())


class Product(BaseModel):
    name: str
    price: float


json_data = '{"name": "Apple", "price": 2.5}'

product = Product.parse_raw(json_data)

print(product)

data = {
    "name": "Banana",
    "price": 10.5
}
product2 = Product.parse_obj(data)
print(product2)





