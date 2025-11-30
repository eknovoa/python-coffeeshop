from register import Register
from order import Order

def welcomeMessage():
  print("\n-- Welcome to Lola's Coffee --")

def displayOptions():
  print("(1) Can I see the menu?\n(2) I am ready to order.\n(3) Exit Shop\n")


def displayMenu():
  print("---------------------------------------------------")
  print("|                                                 |")
  print("|   -- Coffee Menu --                             |")
  print("|  (1) Americano\t $3.50                    |")
  print("|  (2) Cortado\t\t $3.75                    |")
  print("|  (3) Latte\t\t $4.25                    |")
  print("|                                                 |")
  print("|   -- Tea Menu --                                |")
  print("|  (4) Earl Grey\t $2.50                    |")
  print("|  (5) Black\t\t $2.50                    |")
  print("|  (6) Matcha Latte\t $4.25                    |")
  print("|                                                 |")
  print("|   Syrup Options:                                |")
  print("|   Hazlenut, Vanilla,                            |")
  print("|   Sugar-Free Vanilla, Caramel,                  |")
  print("|   Sugar-Free Caramel, Irish Cream               |")
  print("|   $0.25 each                                    |")
  print("|                                                 |")
  print("|   Dairy Alternatives:                           |")
  print("|   Oat, Soy, Almond                              |")
  print("|   $0.50 extra                                   |")
  print("|                                                 |")
  print("|   (7) Add single shot espresso --- $0.50 each   |")
  print("|   (8) Add double shot espresso --- $1.00 each   |")
  print("|                                                 |")
  print("|   -- Food Menu --                               |")
  print("|   (9) Egg bites\t\t $3.50            |")
  print("|  (10) Almond Croissant\t $4.25            |")
  print("|  (11) Chocolate Croissant\t $4.25            |")
  print("|  (12) Croissant\t\t $3.75            |")
  print("|                                                 |")
  print("|                                                 |")
  print("---------------------------------------------------")

def interactWithCustomer(r):
  flag = True
  while flag:
    choice = input("How can I help you today? Please select a number 1-3. --> ")
    match choice:
      case "1":
        displayMenu()
        startOrder(r)
        flag = False
      case "2":
        startOrder(r)
        flag = False
      case "3":
        flag = False
        exit(0)
        break
      case _:
        print("Invalid choice: Please select a number 1-3. --> ")


def startOrder(r):
  order = Order()
  print("Hello, what can I get you today?")
  choice = input("To Order: select a number 1-12 or type 'dairy alternative' or 'syrup'or if you are ready to check out, type 'done'-->")
  while choice != 'done':
    if choice == 'syrup':
      syrup_choice = input("Which syrup would you like:\n(s1) Hazlenut\n(s2) Vanilla\n(s3) Sugar-Free Vanilla\n(s4) Caramel\n(s5) Sugar-Free Caramel\n(s6) Irish Cream\n--> ")
      while syrup_choice != "no":
        order.addItem(syrup_choice)
        syrup_choice = input("Would you like another syrup? If so, type in the syrup choice otherwise type 'no' --> ")

    elif choice == 'dairy alternative':
      dairy_choice = input("Which dairy alternative would you like?\n(d1) soy\n(d2) oat\n(d3) almond\n--> ")
      order.addItem(dairy_choice)
    elif choice in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"):
      order.addItem(choice)
    else:
      print("Please provide a valid option.\n")
    print("\nCan I get you anything else?")
    choice = input("To Order: Select a number 1-12 or type 'dairy alternative' or 'syrup'or if you are ready to check out, type 'done'-->")

  finishOrder(r, order)


def finishOrder(r, order):
  total = order.addTotal()
  order.displayOrder()
  print(f"\nYour total is: ${total:.2f}\n")
  r.addToRegister(order)

def openingTheShop(r):

  
  welcomeMessage()

  displayOptions()
  interactWithCustomer(r)



def closingTheShop(r):
  # run the totals and display a few graphs
  print("\nClosing up for the day! Goodbye and see you tomorrow :)")
  print("---------------------------")
  print("AFTER HOURS:")
  print("\nHi, shop owner! Here is the summary of today's sales:")
  r.printAllOrders()
  # r.showTotalStats()
  # r.showBarChart()
  

if __name__ == "__main__":
  r = Register()

  open_or_close = input("Welcome shop owner, are you ready to (open) or (close) the shop? --> ")
  close = "no"

  while open_or_close != "close" and close != "yes":
    if open_or_close != "open":
      print("Please enter a valid option: type either 'open' or 'close'")
      open_or_close = input("Welcome shop owner, are you ready to (open) or (close) the shop? --> ")
    else:
      if close != "no":
        print("Please enter a valid option: type either 'yes' or 'no'")
      elif close == "yes":
        break
      else:
        openingTheShop(r)
      close = input("Are you ready to close the shop now (yes/no)? --> ")

  closingTheShop(r)