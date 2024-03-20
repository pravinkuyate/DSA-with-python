class item:
    pay_rate=0.5 #class level attribute

    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price

    def total(self):
        return self.quantity* self.price * item.pay_rate

item1=item("sam",2,5)
print(item1.total())






item2=item("pravin",5,1)
item
print(item2.pay_rate)

print(type(item2.pay_rate))

print(item2.__dict__)

item2.pay_rate=0.1

print(item2.total())
    