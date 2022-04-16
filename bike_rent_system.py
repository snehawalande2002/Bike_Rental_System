class Bike:
    def __init__(self,stock):
        self.stock=stock

    def display(self):
        print("Total Bikes: ",self.stock)

    def rent(self,q):

        if q<=0:
            print("Enter proper value")
        elif q>self.stock:
            print("Enter the value (less than stock) ")

        else:
            print("Total price: ",q*100)
            print("Total Bikes: ",self.stock)

while True:
    obj=Bike(100)
    print()
    uc=int(input(''' 1. Display Stock
2. Rent a Bike
3. Exit
                     '''))

    if uc==1:
        obj.display()
    elif uc==2:
        n=int(input("Enter quantity: "))
        obj.rent(n)
    else:
        break

























