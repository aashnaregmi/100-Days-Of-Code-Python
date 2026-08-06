from sqlalchemy import Column, Integer, String, Float

from databasefolder.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
