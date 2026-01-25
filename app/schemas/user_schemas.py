from pydantic import BaseModel

class UserCreate(BaseModel):	# schema for incoming data from frontend
    education: str
    gender: str
    marital_status: str
    last_bill: int
    last_payment: int


class UserResponse(UserCreate):		# schema for data that is to be sent back to frontend/client
    user_id: int

    class Config:
        orm_mode = True   # allows Pydantic to work with SQLAlchemy ORM objects
