class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 *self.radius*self.radius

circle=Circle(S)    
print(f"Circle Area:{circle.area()}")       