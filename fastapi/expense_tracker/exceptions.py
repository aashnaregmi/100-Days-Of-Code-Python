# custom exceptiom
class ExpenseNotFoundException(Exception):
    def __init__(self, expense_id):
        self.expense_id = expense_id


class CategoryNotFoundException(Exception):
    def __init__(self, category):
        self.category = category
