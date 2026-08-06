from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import ExpenseInfo, ExpenseResponse

from exceptions import (
    ExpenseNotFoundException,
    InvalidAmountException,
    CategoryNotFoundException,
)
from handlers import (
    expense_not_found_handler,
    invalid_amount_handler,
    invalid_category_handler,
)
from dependencies import get_current_user
from middleware import register_middleware
from databasefolder.database import Base, SessionLocal, engine
from databasefolder.models import Expense

Base.metadata.create_all(bind=engine)


app = FastAPI()
id = 1

app.add_exception_handler(ExpenseNotFoundException, expense_not_found_handler)


app.add_exception_handler(InvalidAmountException, invalid_amount_handler)


app.add_exception_handler(CategoryNotFoundException, invalid_category_handler)

register_middleware(app)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get(
    "/responsemodel", response_model=list[ExpenseResponse]
)  # list as we ar handling multiple data
def responsemodel(db: Session = Depends(get_db)):

    expenses = db.query(Expense).all()

    return expenses


@app.get("/")
def home(userinfo=Depends(get_current_user)):
    return {
        "msg": f"Hello {userinfo["username"]} ,Welcome to the Expense Tracker website "
    }


# @app.post("/expenses")
# def add_expense(expense: ExpenseInfo, db: Session = Depends(get_db)):
#     if expense.amount <= 0:
#         raise InvalidAmountException(expense.amount)

#     data = {
#         "id": id,
#         "title": expense.title,
#         "amount": expense.amount,
#         "detail": {
#             "category": expense.detail.category,
#             "description": expense.detail.description,
#         },
#     }
#     # expenses.append(data)
#     db.add(data)
#     db.commit()

#     db.refresh(data)

#     return {"message": "Expense added successfully", "expense": expense}


@app.post("/expenses")
def add_expense(expense: ExpenseInfo, db: Session = Depends(get_db)):
    global id
    if expense.amount <= 0:
        raise InvalidAmountException(expense.amount)

    expense_db = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.detail.category,
        description=expense.detail.description,
    )

    db.add(expense_db)
    db.commit()
    db.refresh(expense_db)
    id += 1

    return {"message": "Expense added successfully", "expense": expense_db}


# get all or filter
@app.get("/expenses")
def get_expenses(
    category: str = None, db: Session = Depends(get_db)
):  # if category none then all else according to category
    if category:
        if category:
            expenses_db = db.query(Expense).filter(Expense.category == category).all()
            if len(expenses_db) == 0:  # if ntg in filtered or is empty
                raise CategoryNotFoundException(category)
        return expenses_db

    return db.query(Expense).all()


@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense_db = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense_db:
        raise ExpenseNotFoundException(expense_id)
    return expense_db


@app.put("/expenses/{expense_id}")
def update_expenses(
    expense_id: int, expenseinfo: ExpenseInfo, db: Session = Depends(get_db)
):
    if expenseinfo.amount <= 0:
        raise InvalidAmountException(expenseinfo.amount)
    expense_db = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense_db:
        raise ExpenseNotFoundException(expense_id)
    expense_db.title = expenseinfo.title
    expense_db.amount = expenseinfo.amount
    expense_db.category = expenseinfo.detail.category
    expense_db.description = expenseinfo.detail.description
    db.commit()

    return {"message": "Expense updated successfully"}


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense_db = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense_db:
        raise ExpenseNotFoundException(expense_id)
    db.delete(expense_db)
    db.commit()

    return {"message": f"Id :{expense_id} deleted successfully"}


@app.get("/expense/total")
def get_total(userinfo=Depends(get_current_user), db: Session = Depends(get_db)):
    expenses_db = db.query(Expense).all()

    totalamount = 0

    for expense in expenses_db:
        totalamount += expense.amount

    return {"msg": f"{userinfo['username']}, your total expenses is {totalamount}"}
