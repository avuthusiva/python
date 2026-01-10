class Product:
    quantity = 100
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def read_data(self):
        self.name = input("Please enter the product name: ")
        self.price = input("Please enter the price of the product: ")
    
    def put_data(self):
        print(self.name)
        print(self.price)

#p1 = Product("","")
#p1.read_data()
#p1.put_data()

class DigitalProduct(Product):
    def __init__(self,url):
        self.url = url
    
    def read_url(self):
        self.url = input("Please enter the url :")
    
    def put_url(self):
        print(self.url)

d1 = DigitalProduct("")
d1.read_data()
d1.read_url()
d1.put_data()
d1.put_url()