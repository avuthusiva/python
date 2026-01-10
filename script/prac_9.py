class Product:
    quantity = 100

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount_price(self, discount):
        self.price = self.price - (self.price * discount) / 100
    
    @classmethod
    def info(cls):
        print("Quantity: {}".format(cls.quantity))

p1 = Product("Mobile", 1000)
print(p1.name)
print(p1.price)
p1.discount_price(10)
print(p1.price)
Product.info()