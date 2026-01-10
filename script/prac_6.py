class Product:
    quantity = 100

    def __init__(self,name,price):
        self.name = name
        self.price = price

p1 = Product("Mobile",50000)
print(p1.name)
print(p1.price)
p2 = Product("Laptop","100000")
print(p2.name)
print(p2.price)