class item:
    def __init__(self,name:str,quantity:int):

        assert quantity> 0,f"{quantity } is not greator than zero"

        self.name=name
        self.quantity=quantity




item1=item("prav",0)


