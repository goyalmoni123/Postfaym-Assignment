from pydantic import BaseModel


class WithdrawalCreate(BaseModel):
    user_id: int
    amount: float


class WithdrawalResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    status: str

    class Config:
        from_attributes = True