class Cricle:
    @staticmethod
    def area(radius):
        return 3.14 * radius * radius
    
    @staticmethod
    def perimeter(radius):
        return 2 * 3.14 * radius
    
a = Cricle.area(10)
p = Cricle.perimeter(10)
print("Area:", a)
print("Perimeter:", p)