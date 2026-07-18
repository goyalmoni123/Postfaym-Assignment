from pydantic import BaseModel
from typing import Optional


class ReconcileRequest(BaseModel):
    status: str   # Approved / Rejected


class WithdrawRequest(BaseModel):
    user_id: int


class PayoutResponse(BaseModel):
    message: str
    amount: Optional[float] = None