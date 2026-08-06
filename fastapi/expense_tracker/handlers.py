from fastapi import Request
from fastapi.responses import JSONResponse


from exceptions import (
    ExpenseNotFoundException,
    CategoryNotFoundException,
)

# @app.exception_handler() is a decorator-based registration, useful for
# small applications. In larger applications, we separate handlers into
# different files and register them using app.add_exception_handler() to
# keep code modular and avoid circular imports. Both methods work the same internally.


async def expense_not_found_handler(request: Request, exc: ExpenseNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Expense with id {exc.expense_id} not found"},
    )


async def invalid_category_handler(request: Request, exc: CategoryNotFoundException):
    return JSONResponse(
        status_code=400,
        content={"message": f"Category:{exc.category} not found"},
    )
