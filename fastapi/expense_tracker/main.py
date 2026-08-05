from fastapi import FastAPI, Depends

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

app = FastAPI()
id = 1

app.add_exception_handler(ExpenseNotFoundException, expense_not_found_handler)


app.add_exception_handler(InvalidAmountException, invalid_amount_handler)


app.add_exception_handler(CategoryNotFoundException, invalid_category_handler)

register_middleware(app)

expenses = []


@app.get(
    "/responsemodel", response_model=list[ExpenseResponse]
)  # list as we ar handling multiple data
def responsemodel():
    return expenses


@app.get("/")
def home(userinfo=Depends(get_current_user)):
    return {
        "msg": f"Hello {userinfo["username"]} ,Welcome to the Expense Tracker website "
    }


@app.post("/expenses")
def add_expense(expense: ExpenseInfo):
    if expense.amount <= 0:
        raise InvalidAmountException(expense.amount)
    global id

    data = {
        "id": id,
        "title": expense.title,
        "amount": expense.amount,
        "detail": {
            "category": expense.detail.category,
            "description": expense.detail.description,
        },
    }
    expenses.append(data)
    id += 1
    return {"message": "Expense added successfully", "expense": expense}


# get all or filter
@app.get("/expenses")
def get_expenses(
    category: str = None,
):  # if category none then all else according to category
    if category:
        filtered = []  # because if no this then the 1 item will  only be retuned
        for e in expenses:
            if e["detail"]["category"] == category:

                filtered.append(e)
        if len(filtered) == 0:  # if ntg in filtered or is empty
            raise CategoryNotFoundException(category)
        return filtered

    return expenses


@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    for e in expenses:
        if e["id"] == expense_id:
            return e
    raise ExpenseNotFoundException(expense_id)


@app.put("/expenses/{expense_id}")
def update_expenses(expense_id: int, expenseinfo: ExpenseInfo):
    if expenseinfo.amount <= 0:
        raise InvalidAmountException(expenseinfo.amount)
    for e in expenses:
        if e["id"] == expense_id:
            e["title"] = expenseinfo.title
            e["amount"] = expenseinfo.amount

            e["detail"] = {
                "category": expenseinfo.detail.category,
                "description": expenseinfo.detail.description,
            }

            return {"message": "Expense updated successfully"}
    raise ExpenseNotFoundException(expense_id)


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    for e in expenses:
        if e["id"] == expense_id:
            expenses.remove(e)
            return {"message": f"Id :{expense_id} deleted successfully"}
    raise ExpenseNotFoundException(expense_id)


@app.get("/expense/total")
def get_total(userinfo=Depends(get_current_user)):
    totalamount = 0
    for expense in expenses:
        totalamount += expense["amount"]
    return {"msg": f"{userinfo["username"]},your total expenses is {totalamount}"}
