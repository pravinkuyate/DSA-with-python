class item:
    def __init__(self,name:str,quantity:int):
        assert quantity >0

        #asssign object

        self.name=name
        self.quantity=quantity
    def pr(self):
        self.quantity+=10







item1=item("pravin",50)
item1.pr()
item1.hs="pravinss"
print(item1.quantity)
print(item1.hs)

