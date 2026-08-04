# custom exceptiom
class ExpenseNotFoundException(Exception):
    def __init__(self, expense_id):
        self.expense_id = expense_id


class InvalidAmountException(Exception):
    def __init__(self, amount):
        self.amount = amount


class CategoryNotFoundException(Exception):
    def __init__(self, category):
        self.category = category
