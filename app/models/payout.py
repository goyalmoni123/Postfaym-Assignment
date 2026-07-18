from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Payout(Base):
    __tablename__ = "payouts"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    sale_id = Column(Integer, ForeignKey("sales.id"))

    amount = Column(Float, default=0)

    payout_type = Column(String, default="Advance")
    # Advance / Final / Withdrawal

    status = Column(String, default="Pending")
    # Pending / Approved / Rejected / Failed / Completed

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    retry_count = Column(Integer, default=0)

    user = relationship("User")

    sale = relationship("Sale")