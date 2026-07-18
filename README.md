# Postfaym User Payout Management System

## Overview

The Postfaym User Payout Management System is a FastAPI-based backend application that manages user sales and payout workflows.

The system allows users to:

- Create users
- Create sales
- Calculate 10% advance payout
- Perform final reconciliation
- Withdraw wallet balance
- Recover failed payouts
- View payout history

This project was developed as part of the Postfaym SDE Intern Assignment.

---

## Tech Stack

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

## Features

### User Management

- Create User
- Get User(s)

### Sales Management

- Create Sale

### Wallet Management

- Automatic wallet creation
- Wallet balance update

### Advance Payout

- Calculates 10% advance on pending sales
- Updates wallet balance
- Creates payout record

### Final Reconciliation

Supports:

- Approved
- Rejected

If approved:

- Remaining 90% is credited.

If rejected:

- No final payout is generated.

### Withdrawal

- Withdraw available wallet balance
- Enforces 24-hour withdrawal rule

### Failed Payout Recovery

- Retry failed payouts
- Update payout status

### Payout History

- Shows complete payout history for a user.

---

## Project Structure

```
Postfaym-Assignment
│
├── app
│   ├── models
│   ├── routers
│   ├── schema
│   ├── services
│   ├── utils
│   ├── database.py
│   └── main.py
│
├── requirements.txt
├── README.md
├── LLD.md
├── postfaym.db
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run server

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Users

POST

```
/users/
```

GET

```
/users/
```

GET

```
/users/{user_id}
```

---

### Sales

POST

```
/sales/
```

---

### Payout

POST

```
/payout/advance/{user_id}
```

POST

```
/payout/reconcile/{sale_id}
```

POST

```
/payout/withdraw/{user_id}
```

POST

```
/payout/recover/{payout_id}
```

GET

```
/payout/history/{user_id}
```

---

## Database Tables

- Users
- Sales
- Wallets
- Payouts
- Withdrawals

---

## Future Improvements

- Authentication using JWT
- Background payout processing
- Admin Dashboard
- Email Notifications
- Payment Gateway Integration

---

## Author

Monika Goyal