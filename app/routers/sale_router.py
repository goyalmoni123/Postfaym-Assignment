from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.sale import Sale
from app.schema.sale_schema import SaleCreate, SaleResponse

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


@router.post("/", response_model=SaleResponse)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):

    new_sale = Sale(
    user_id=sale.user_id,
    brand=sale.brand,
    earning=sale.earning,
    status="Pending"
)

    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)

    return new_sale