class Category:
  ledger = {}
  
  def __init__(self, category_name):
    self.category_name = category_name


  def deposit(self, amount, description = None):
    self.amount = amount
    self.description = description
    self.ledger[self.category_name] = [self.amount, self.description]

  def withdraw(self, amount, ):





def create_spend_chart(categories):
  pass