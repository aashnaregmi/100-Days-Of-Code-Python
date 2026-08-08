from pydantic import BaseModel, Field


# Nested model
class ExpenseDetail(BaseModel):
    category: str
    description: str


# Request model (data coming from client)
class ExpenseInfo(BaseModel):
    title: str
    amount: float = Field(gt=0)
    detail: ExpenseDetail


# Response model (data going back to client)
class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    description: str
