from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_data = {
    "id": 1,
    "username": "zara",
    "email": "zara@combat.com",
}

user = User(**user_data)
