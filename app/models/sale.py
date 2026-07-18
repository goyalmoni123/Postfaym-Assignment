from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    brand = Column(String, nullable=False)

    status = Column(String, default="Pending")

    earning = Column(Float, nullable=False)

    advance_paid = Column(Boolean, default=False)

    advance_amount = Column(Float, default=0)

    user = relationship("User", back_populates="sales")