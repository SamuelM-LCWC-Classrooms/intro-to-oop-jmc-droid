class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def get_area(self):
        area = 3.141 * (self.radius ** 2)
        return round(area)
    
    def get_perimeter(self):
        perimeter = 2 * 3.141 * self.radius
        return round(perimeter) 
    

circy = Circle(11)
print(circy.get_area())

circy = Circle(4.44)
print(circy.get_perimeter())