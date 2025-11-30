from data import shopItems

class Order:

  def __init__(self):
    self.order = []
    self.orderToPrint = []
  
  def addItem(self,item):
    self.order.append(item)

  def addTotal(self):
    total = 0.0
    for item in self.order:
      if item in shopItems["syrups"]:
        for key, value in shopItems["syrups"][item].items():
          total += value
          self.orderToPrint.append(key + " syrup")
      elif item in shopItems["dairy alternatives"]:
        for key, value in shopItems["dairy alternatives"][item].items():
          total += value
          self.orderToPrint.append(key + " milk")
      else:
        for key, value in shopItems[item].items():
          total += value
          self.orderToPrint.append(key)
    return total

  def displayOrder(self):
    print("\nYou ordered:")
    for item in self.orderToPrint:
      print(f"- {item}")