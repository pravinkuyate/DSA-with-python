class item:
    all=[]
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price

        item.all.append(self)

    def __repr__(self):
        return f"item('{self.name}','{self.quantity}','{self.price}')"
    


item1=item("pra",2,4)
item2=item("sam",5,4)
item3=item("nok",8,10)
item4=item("leno",5,10)


print(item.all)



    


