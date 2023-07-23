import math

class Shape:
        
    def __init__(self, type, name="Shape"):
        self.name = name                
        self.type = type                
        self.perimeter = None           
        self.area = None        
        


class Circle(Shape):
    
    def __init__(self, radius):
        super().__init__("Circular", "Circle")
        self.perimeter = self.get_perimeter(radius)
        self.area = self.get_area(radius)
    
    def get_perimeter(self, radius):
        return 2 * math.pi * radius    
    
    def get_area(self, radius):
        return math.pi * radius * radius   
    
    
    
class Polygon(Shape):
    
    def __init__(self, name):
        super().__init__("Polygon", name)
        
        
        
class Triangle(Polygon):
    
    is_valid = False
    
    def __init__(self, a, b, c):
        super().__init__("Triangle") 
        self.is_valid = self.check_validity(a, b, c) 
        self.perimeter = self.get_perimeter(a, b, c)
        self.area = self.get_area(a,b,c)
        
        
    def check_validity(self, a, b, c):
        if (a + b <= c or a + c <= b or b + c <= a):
            print("Attempt to create a triangle with incorrect values")
            return False
        return True
        

    def get_perimeter(self, a, b, c):
        if self.is_valid:
            return a + b + c            
        
    def get_area(self,a, b, c):
        if self.is_valid:
            s = (a + b + c) / 2.0
            return math.sqrt(s * (s-a) * (s-b) * (s-c))    


    
class Rectangle(Polygon):
    
    def __init__(self, height, width, name="Rectangle"):   
        super().__init__(name)
        self.perimeter = self.get_perimeter(height, width)
        self.area = self.get_area(height, width)
            
    def get_area(self, height, width):
        return height * width          
        
    def get_perimeter(self, height, width):
        return 2 * (height + width)    



class Square(Rectangle):
    
    def __init__(self, height):                     
       super().__init__(height, height, "Square")     



class Pentagon(Polygon):
    
    def __init__(self, side):           
        super().__init__("Pentagon")    
        self.perimeter = self.get_perimeter(side)
        self.area = self.get_area(side)
        
    def get_area(self, a):
        return (0.25 * a * a * math.sqrt(5.0 * (5.0 + (2.0 * math.sqrt(5)))))
        
    def get_perimeter(self, side):
        return 5*side      
    
    
    
class Hexagon(Polygon):
    
    def __init__(self, side):
        super().__init__("Hexagon")              
        self.perimeter = self.get_perimeter(side)
        self.area = self.get_area(side)
        
    def get_area(self, a):
        return (1.5 * a * a * math.sqrt(3))
        
    def get_perimeter(self, side):
        return (6*side)     # all side are same
        
            
if __name__ == '__main__':
    
    # Circle Object
    my_circle = Circle(2)
    
    # Triangle Object (Invalid)
    my_triangle = Triangle(3, 1.7, 4.9)
    
    # Triangle Object (Valid)
    my_triangle = Triangle(3, 7, 4.6)
    
    # Rectangle Object
    my_rectangle = Rectangle(3, 4.5)
    
    # Square Object
    my_square = Square(4)
    
    # Pentagon Object
    my_pentagon = Pentagon(3)
    
    # Hexagon Object
    my_hexagon = Hexagon(3)
    
    
    print("\nCircle perimeter and area: ")
    print(my_circle.perimeter)
    print(my_circle.area)

    print("\nTriangle perimeter and area: ")
    print(my_triangle.perimeter)
    print(round(my_triangle.area, 3))

    print("\nRectangle perimeter and area: ")
    print(my_rectangle.perimeter)
    print(round(my_rectangle.area, 3))
    
    print("\nSquare perimeter and area: ")
    print(my_square.perimeter)
    print(round(my_square.area, 3))
    
    print("\nPentagon perimeter and area: ")
    print(my_pentagon.perimeter)
    print(round(my_pentagon.area, 3))
    
    print("\nHexagon perimeter and area: ")
    print(my_hexagon.perimeter)
    print(round(my_hexagon.area, 3))