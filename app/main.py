from fastapi import FastAPI

from app.database import engine, Base

from app.routers.user_router import router as user_router
from app.routers.sale_router import router as sale_router
from app.routers.payout_router import router as payout_router

from app.models.user import User
from app.models.sale import Sale
from app.models.wallet import Wallet
from app.models.withdrawal import Withdrawal
from app.models.payout import Payout


app = FastAPI(
    title="Postfaym User Payout Management System",
    description="SDE Intern Assignment",
    version="1.0.0"
)


Base.metadata.create_all(bind=engine)


app.include_router(user_router)
app.include_router(sale_router)
app.include_router(payout_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Postfaym User Payout Management System"
    }