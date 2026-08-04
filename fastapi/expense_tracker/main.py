from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import Depends

app = FastAPI()
id = 1


# responsemodel rn just for undertanding
class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float


# nested pydantic
class ExpenseDetail(BaseModel):
    category: str
    description: str


class ExpenseInfo(BaseModel):
    title: str
    amount: float
    detail: ExpenseDetail


# custom exceptiom
class ExpenseNotFoundException(Exception):
    def __init__(self, expense_id):
        self.expense_id = expense_id


@app.exception_handler(ExpenseNotFoundException)
async def expense_not_found_handler(request: Request, exc: ExpenseNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Expense with id {exc.expense_id} not found"},
    )


class InvalidAmountException(Exception):
    def __init__(self, amount):
        self.amount = amount


@app.exception_handler(InvalidAmountException)
async def invalid_amount_handler(request: Request, exc: InvalidAmountException):
    return JSONResponse(
        status_code=400,
        content={
            "message": f"Invalid amount: {exc.amount}. Amount must be greater than 0"
        },
    )


class CategoryNotFoundException(Exception):
    def __init__(self, category):
        self.category = category


@app.exception_handler(CategoryNotFoundException)
async def invalid_category_handler(request: Request, exc: CategoryNotFoundException):
    return JSONResponse(
        status_code=400,
        content={"message": f"Category:{exc.category} not found"},
    )


# Fake User Authentication for now learning purpose
def get_current_user():
    return {"username": "Ashna", "role": "admin"}


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
