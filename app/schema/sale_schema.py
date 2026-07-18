from pydantic import BaseModel


class SaleCreate(BaseModel):
    user_id: int
    brand: str
    earning: float


class SaleResponse(BaseModel):
    id: int
    user_id: int
    brand: str
    earning: float
    status: str
    advance_paid: bool
    advance_amount: float

    class Config:
        from_attributes = True