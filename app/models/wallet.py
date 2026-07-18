from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    withdrawable_balance = Column(Float, default=0)

    advance_paid = Column(Float, default=0)

    final_paid = Column(Float, default=0)

    last_withdrawal_time = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="wallet")