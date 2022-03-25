class Category:
  
  def __init__(self, category_name):
    self.category_name = category_name
    self.ledger = []

  def deposit(self, amount, description = ''):
    self.amount = amount
    self.description = description
    self.ledger.append({"amount": self.amount, "description":self.description})
  
  def withdraw(self, amount, description = ''):
    self.amount = amount
    self.description = description
    self.more = self.check_funds(amount)
    for x in self.ledger:
      if self.more == True and 'depos' in x["description"]:
        self.ledger.append({"amount": -self.amount, "description":self.description})
        return True
      elif self.more == True and 'Transfer from ' in x["description"]:
        self.ledger.append({"amount": -self.amount, "description":self.description})
        return True
      else:
          return False

  def get_balance(self):
    deposit = 0
    dict_key = list(map(lambda x: x['description'], self.ledger))
    dict_value = list(map(lambda x: x['amount'], self.ledger))
    dict_keys = dict_key
    if len(dict_keys) > 0:
      for i in dict_keys:
        if 'deposit' in i or 'Transfer from ' in i:
          index = dict_key.index(i)
          deposit = dict_value[index]
          dict_key.pop(index), dict_value.pop(index)
          if len(dict_value) > 0:
            withdraw_items = sum(dict_value)
            balance = deposit - abs(withdraw_items)
            return balance
          elif len(dict_value) == 0:
            balance = deposit
            return balance
    else:
      balance = 0
      return balance

  def check_funds(self, amount):
    balancer = self.get_balance()
    if balancer >= amount:
      return True
    else:
      return False

  def transfer(self, amount, category):
    self.amount = amount
    check_balance = self.check_funds(self.amount)
    if check_balance == True:
      deposit_name_to = 'Transfer to ' + category.category_name
      deposit_name_from = 'Transfer from ' + self.category_name
      self.withdraw(amount, deposit_name_to)
      #self.ledger.append({"amount": -self.amount, "description": deposit_name_to})
      category.deposit(self.amount, deposit_name_from)
      return True
    elif check_balance == False:
      return False
      
  
  def __str__(self):
    lister = []
    len_category_name = len(self.category_name)
    stars_string = '*'*((30 - len_category_name)//2)
    first_string = stars_string + self.category_name + stars_string
    lister.append(first_string)

    list_key = list(map(lambda x: x['description'], self.ledger))
    list_value = list(map(lambda x: format(float(x['amount']), '.2f'), self.ledger))

    for i in list_value:
      len_value = len(i)
      index = list_value.index(i)
      if list_key[index] != '' and len(list_key[index])>23:
        key = list_key[index][:23]
        len_whitespace = ' '*(30-len(key)-len_value)
      elif list_key[index] != '' and len(list_key[index]) <= 23:
        len_key = len(list_key[index])
        len_whitespace = ' '*(30-len_key-len_value)
      else:
        len_key = 0
        len_whitespace = ' '*(30-len_key-len_value)

      if list_key[index] != '':
        if len(list_key[index])>23:
          strings = list_key[index][:23] + len_whitespace + i
        elif len(list_key[index]) <= 23:
          strings = list_key[index] + len_whitespace + i          
      else:
        strings = len_whitespace + i
      lister.append(strings)
    
    last_string = 'Total: ' + str(self.get_balance())
    lister.append(last_string)
    total = ('\n'.join(lister))
    return total

def create_spend_chart(categories):
  category_names = list(map(lambda x: x.category_name, categories))
  category_list = []
    
  for i in categories:
    categori_amount = list(map(lambda x: x['amount'], i.ledger))
    categori_description = list(map(lambda x: x['description'], i.ledger))
    categori_descriptions = categori_description
    #if len(categori_descriptions) > 0:
    for y in categori_descriptions:
      if 'deposit' in y or 'Transfer from ' in y:
        index = categori_description.index(y)
        categori_amount.pop(index)
        category_list.append(sum(categori_amount))

  sum_spent_amount = sum(category_list)
  persent_spent_amount = list(map(lambda x: round(x/sum_spent_amount*10,2), category_list))
  dict_cat_per = dict(zip(category_names, persent_spent_amount))
  
  list_null, list_ten, list_20, list_30, list_40, list_50, list_60, list_70,list_80, list_90, list_100 = [],[],[],[],[],[],[],[],[],[],[]
  for i in range(0, 110, 10):
    if i == 0:
      stringa = '  '+str(i)+'| '
      list_null.append(stringa)
    elif i == 10:
      stringa = ' ' + str(i)+'| '
      list_ten.append(stringa)
    elif i == 20:
      stringa = ' '+str(i)+'| '
      list_20.append(stringa)
    elif i == 30:
      stringa = ' '+str(i)+'| '
      list_30.append(stringa)
    elif i == 40:
      stringa = ' '+str(i)+'| '
      list_40.append(stringa)
    elif i == 50:
      stringa = ' ' + str(i)+'| '
      list_50.append(stringa)
    elif i == 60:
      stringa = ' '+str(i)+'| '
      list_60.append(stringa)
    elif i == 70:
      stringa = ' '+str(i)+'| '
      list_70.append(stringa)
    elif i == 80:
      stringa = ' ' + str(i)+'| '
      list_80.append(stringa)
    elif i == 90:
      stringa = ' '+str(i)+'| '
      list_90.append(stringa)
    elif i == 100:
      stringa = str(i)+'| '
      list_100.append(stringa)

  for i in category_names:
    for y in range(0,11):
      if y == 0:
        if dict_cat_per[i] > 0:
          list_null.append('o  ')
          dict_cat_per[i]=dict_cat_per[i]-1
        elif dict_cat_per[i] < 0:
          list_null.append('   ')
      elif y == 1:
        if dict_cat_per[i] > 0:
          list_ten.append('o  ')
          dict_cat_per[i]=dict_cat_per[i]-1
        elif dict_cat_per[i] < 0:
          list_ten.append('   ')
      elif y == 2:
        if dict_cat_per[i] > 0:
          list_20.append('o  ')
          dict_cat_per[i]=dict_cat_per[i]-1
        elif dict_cat_per[i] < 0:
          list_20.append('   ')
      elif y == 3:
        if dict_cat_per[i] > 0:
          list_30.append('o  ')
          dict_cat_per[i]=dict_cat_per[i]-1
        elif dict_cat_per[i] < 0:
          list_30.append('   ')
      elif y == 4:
        if dict_cat_per[i] > 0:
          list_40.append('o  ')
          dict_cat_per[i]=dict_cat_per[i]-1
        elif dict_cat_per[i] < 0:
          list_40.append('   ')
      elif y == 5:
        if dict_cat_per[i] > 0:
          list_50.append('o  ')
          dict_cat_per[i]=dict_cat_per[i]-1
        elif dict_cat_per[i] < 0:
          list_50.append('   ')
      elif y == 6:
        if dict_cat_per[i] > 0:
          list_60.append('o  ')
          dict_cat_per[i]=dict_cat_per[i]-1
        elif dict_cat_per[i] < 0:
          list_60.append('   ')
      elif y == 7:
        if dict_cat_per[i] > 0:
          list_70.append('o  ')
          dict_cat_per[i]=dict_cat_per[i]-1
        elif dict_cat_per[i] < 0:
          list_70.append('   ')
      elif y == 8:
        if dict_cat_per[i] > 0:
          list_80.append('o  ')
          dict_cat_per[i]=dict_cat_per[i]-1
        elif dict_cat_per[i] < 0:
          list_80.append('   ')
      elif y == 9:
        if dict_cat_per[i] > 0:
          list_90.append('o  ')
          dict_cat_per[i]=dict_cat_per[i]-1
        elif dict_cat_per[i] < 0:
          list_90.append('   ')
      elif y == 10:
        if dict_cat_per[i] > 0:
          list_100.append('o  ')
          dict_cat_per[i]=dict_cat_per[i]-1
        elif dict_cat_per[i] < 0:
          list_100.append('   ')
  
  second_to_last_list = ['    -'+'-'*(3*len(category_names)),list_null, list_ten, list_20, list_30, list_40, list_50, list_60, list_70, list_80, list_90, list_100, 'Percentage spent by category']
  second_to_last_list.reverse()

  max_item = max(list(map(lambda x: len(list(x)), category_names)))
  category_names_list = list(map(lambda x: list(x), category_names))

  x = []
  for i in range(0, max_item):
    for y in category_names_list:
      if len(y) < max_item:
        y.extend(' ')
  
  for i in range(0, max_item):
    temporary_list = []
    for y in category_names_list:
      if category_names_list[0] == y:
        if len(y) > 0:
          last_element = y.pop()
          temporary_list.append('     '+last_element)
        elif len(y) == 0:
          temporary_list.append('     ')
      elif category_names_list[-1] == y:
        if len(y) > 0:
          last_element = y.pop()
          temporary_list.append('  '+last_element+'  ')
        elif len(y) == 0:
          temporary_list.append('  '+'    ')
      else:
        if len(y) > 0:
          last_element = y.pop()
          temporary_list.append('  '+last_element)
        elif len(y) == 0:
          temporary_list.append('  ')
    x.append(temporary_list)
  x.reverse()
  for i in x:
    second_to_last_list.append(i)
  #second_to_last_list.reverse()  
  last_list = list(map(lambda x: ('').join(x), second_to_last_list))
  return ('\n').join(last_list)
  
