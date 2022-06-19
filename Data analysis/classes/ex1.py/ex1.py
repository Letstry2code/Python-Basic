class Pizza:
    def __init__(self,topping,size,price):
        self.topping=topping
        self.size=size
        self.price=price
    
    def __str__(self):
        return f"Pizza({self.topping} {self.size}) -> {self.price}"

if __name__=="__main__":
    p1=Pizza("Pepperoni","medium",310)
    p2=Pizza("Mushroom","small",230)
    p3=Pizza("Paneer","large",360)
    p4=Pizza("Corn","medium",210)
    print(p1)
    print(p2)
    print(p3)
    print(p4)