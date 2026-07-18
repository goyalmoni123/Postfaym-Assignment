from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Withdrawal(Base):
    __tablename__ = "withdrawals"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    amount = Column(Float, nullable=False)

    status = Column(String, default="Pending")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship("User", back_populates="withdrawals")