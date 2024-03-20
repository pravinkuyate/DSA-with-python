class item:
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price

    def total(self):
        return self.quantity* self.price
    

item2=item("pravin",500,10)
item
print(item2.total())



