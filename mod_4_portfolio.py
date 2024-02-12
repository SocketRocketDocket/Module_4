
class ItemToPurchase:
    #Constructor default values, initilize names
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = int(item_price)
        self.item_quantity = int(item_quantity)
    #Method for total_cost
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")
    
item1 = ItemToPurchase(input('Enter the item name: '), int(input('Enter the item price: ')), float(input('Enter the item quantity: ')))
item1.print_item_cost()

item2 = ItemToPurchase(input('Enter the item name: '), int(input('Enter the item price: ')), float(input('Enter the item quantity: ')))
item2.print_item_cost()

total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity
print(f"Total: ${total_cost}")