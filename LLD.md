# Low Level Design (LLD)

# Postfaym User Payout Management System

## Objective

Build a backend payout management system where users can create sales, receive advance payouts, perform final reconciliation, withdraw money, recover failed payouts, and maintain payout history.

---

# Technology

- FastAPI
- SQLAlchemy
- SQLite
- Python
- Pydantic

---

# Modules

## User Module

Responsibilities

- Create User
- Fetch Users

Tables

- Users
- Wallet

---

## Sales Module

Responsibilities

- Create Sale
- Track Sale Status

States

- Pending
- Approved
- Rejected

---

## Wallet Module

Responsibilities

- Store withdrawable balance
- Store advance paid
- Store final paid

---

## Payout Module

Responsibilities

Advance Payout

- Calculate 10%
- Update wallet
- Create payout record

Final Reconciliation

Approved

- Credit remaining 90%

Rejected

- No payment

Withdrawal

- Withdraw wallet balance
- Apply 24-hour restriction

Recovery

- Retry failed payouts

History

- Display payout history

---

# Database Design

## Users

- id
- name
- email

---

## Sales

- id
- user_id
- brand
- earning
- status
- advance_paid
- advance_amount

---

## Wallet

- id
- user_id
- withdrawable_balance
- advance_paid
- final_paid
- last_withdrawal_time

---

## Payout

- id
- user_id
- sale_id
- amount
- payout_type
- status
- retry_count
- created_at

---

## Withdrawal

- id
- user_id
- amount
- created_at

---

# Business Flow

User Created

↓

Wallet Created

↓

Sale Created

↓

Advance Payout (10%)

↓

Reconciliation

↓

Approved → Remaining 90%

↓

Rejected → No Final Payment

↓

Withdrawal

↓

Recovery (if payout failed)

↓

History

---

# Business Rules

- Advance payout = 10%
- Remaining payout = 90%
- Only approved sales receive final payout
- Withdrawal allowed once every 24 hours
- Failed payouts can be retried
- Wallet balance updates after every successful payout

---

# API Flow

Create User

↓

Create Sale

↓

Advance Payout

↓

Reconcile

↓

Withdrawal

↓

Recovery

↓

History

---

# Conclusion

The system provides a modular and scalable payout management solution using FastAPI and SQLAlchemy. It supports advance payouts, final reconciliation, withdrawals, recovery of failed payouts, and complete payout tracking through history.