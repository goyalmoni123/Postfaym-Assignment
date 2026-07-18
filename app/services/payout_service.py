from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from app.models.sale import Sale
from app.models.wallet import Wallet
from app.models.payout import Payout


# ----------------------------
# Advance Payout
# ----------------------------
def calculate_advance_payout(user_id: int, db: Session):

    pending_sales = db.query(Sale).filter(
        Sale.user_id == user_id,
        Sale.status == "Pending",
        Sale.advance_paid == False
    ).all()

    if not pending_sales:
        return {
            "message": "No pending sales found"
        }

    wallet = db.query(Wallet).filter(
        Wallet.user_id == user_id
    ).first()

    if not wallet:
        return {
            "message": "Wallet not found"
        }

    total_pending = 0
    total_advance = 0

    for sale in pending_sales:

        advance = sale.earning * 0.10

        total_pending += sale.earning
        total_advance += advance

        sale.advance_paid = True
        sale.advance_amount = advance

        wallet.withdrawable_balance += advance
        wallet.advance_paid += advance

        payout = Payout(
            user_id=user_id,
            sale_id=sale.id,
            amount=advance,
            payout_type="Advance",
            status="Completed"
        )

        db.add(payout)

    db.commit()
    db.refresh(wallet)

    return {
        "message": "Advance payout successful",
        "total_pending": total_pending,
        "advance_amount": total_advance,
        "wallet_balance": wallet.withdrawable_balance
    }


# ----------------------------
# Final Reconciliation
# ----------------------------
def reconcile_payout(
    sale_id: int,
    decision: str,
    db: Session
):

    sale = db.query(Sale).filter(
        Sale.id == sale_id
    ).first()

    if not sale:
        return {
            "message": "Sale not found"
        }

    wallet = db.query(Wallet).filter(
        Wallet.user_id == sale.user_id
    ).first()

    if not wallet:
        return {
            "message": "Wallet not found"
        }

    if decision.lower() == "approved":

        final_amount = sale.earning - sale.advance_amount

        wallet.withdrawable_balance += final_amount
        wallet.final_paid += final_amount

        payout = Payout(
            user_id=sale.user_id,
            sale_id=sale.id,
            amount=final_amount,
            payout_type="Final",
            status="Approved"
        )

        db.add(payout)

        sale.status = "Approved"

    else:

        wallet.withdrawable_balance -= sale.advance_amount
        wallet.advance_paid -= sale.advance_amount

        payout = Payout(
            user_id=sale.user_id,
            sale_id=sale.id,
            amount=sale.advance_amount,
            payout_type="Recovery",
            status="Rejected"
        )

        db.add(payout)

        sale.status = "Rejected"

    db.commit()

    return {
        "message": f"Sale {decision} successfully"
    }


# ----------------------------
# Withdrawal (24 Hours Rule)
# ----------------------------
def withdraw_amount(
    user_id: int,
    db: Session
):

    wallet = db.query(Wallet).filter(
        Wallet.user_id == user_id
    ).first()

    if not wallet:
        return {
            "message": "Wallet not found"
        }

    if wallet.withdrawable_balance <= 0:
        return {
            "message": "No balance available"
        }

    if wallet.last_withdrawal_time:

        next_time = wallet.last_withdrawal_time + timedelta(hours=24)

        if datetime.utcnow() < next_time:
            return {
                "message": "Withdrawal allowed only after 24 hours"
            }

    amount = wallet.withdrawable_balance

    wallet.withdrawable_balance = 0
    wallet.last_withdrawal_time = datetime.utcnow()

    db.commit()

    return {
        "message": "Withdrawal successful",
        "amount": amount
    }


# ----------------------------
# Failed Payout Recovery
# ----------------------------
def retry_failed_payout(
    payout_id: int,
    db: Session
):

    payout = db.query(Payout).filter(
        Payout.id == payout_id
    ).first()

    if not payout:
        return {
            "message": "Payout not found"
        }

    payout.status = "Completed"
    payout.retry_count += 1

    db.commit()

    return {
        "message": "Payout recovered successfully"
    }


# ----------------------------
# Payout History
# ----------------------------
def payout_history(
    user_id: int,
    db: Session
):

    payouts = db.query(Payout).filter(
        Payout.user_id == user_id
    ).all()

    return payouts