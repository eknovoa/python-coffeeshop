from shopData import shopPrices

class Register:
  
  def __init__(self):
    self.orders = []
    self.totalSales = 0.0

  def addToRegister(self, order):
    self.orders.append(order)
  
  def createFrequencyMap(self):
    frequency = {}
    for order in self.orders:
        for item in order.orderToPrint:
          if item in frequency:
            frequency[item] += 1
          else:
            frequency[item] = 1
    return frequency

  def getTotalSales(self):
    freqOrders = self.createFrequencyMap()
    for key, value in freqOrders.items():
      self.totalSales +=  (value * shopPrices[key])
    return self.totalSales

  def printAllOrders(self):
    if len(self.orders) > 0:
      freqOrders = self.createFrequencyMap()
      for key, value in freqOrders.items():
        if value > 1 and key != "egg bites":
          print(f'- {value} {key}s')
        else:
          print(f'- {value} {key}')
      print("---------------")
      print(f'Total Sales: ${self.getTotalSales():.2f}\n')
    else:
      print("No sales today :(\nBut hopefully tomorrow we get more customers.")

 