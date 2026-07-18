from pydantic import BaseModel


class WalletCreate(BaseModel):
    user_id: int


class WalletResponse(BaseModel):
    id: int
    user_id: int
    withdrawable_balance: float
    advance_paid: float
    final_paid: float

    class Config:
        from_attributes = True