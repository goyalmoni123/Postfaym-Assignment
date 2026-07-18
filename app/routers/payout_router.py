from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.payout_service import (
    calculate_advance_payout,
    reconcile_payout,
    withdraw_amount,
    retry_failed_payout,
    payout_history
)
from app.schema.payout_schema import ReconcileRequest

router = APIRouter(
    prefix="/payout",
    tags=["Payout"]
)


@router.post("/advance/{user_id}")
def create_advance_payout(
    user_id: int,
    db: Session = Depends(get_db)
):
    return calculate_advance_payout(user_id, db)


@router.post("/reconcile/{sale_id}")
def reconcile(
    sale_id: int,
    request: ReconcileRequest,
    db: Session = Depends(get_db)
):
    return reconcile_payout(
        sale_id,
        request.status,
        db
    )


@router.post("/withdraw/{user_id}")
def withdraw(
    user_id: int,
    db: Session = Depends(get_db)
):
    return withdraw_amount(
        user_id,
        db
    )


@router.post("/recover/{payout_id}")
def recover(
    payout_id: int,
    db: Session = Depends(get_db)
):
    return retry_failed_payout(
        payout_id,
        db
    )


@router.get("/history/{user_id}")
def history(
    user_id: int,
    db: Session = Depends(get_db)
):
    return payout_history(
        user_id,
        db
    )