class Rectangle:
    def __init__(self,length,width) -> None:
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*self.length+2*self.width

''' Withou Super class '''
class Square:
    def __init__(self,length) -> None:
        self.length=length
        

    def area(self):
        return self.length*self.length

    def perimeter(self):
        return 2*self.length+2*self.length

''' Using Super'''
class WithSuperSquare(Rectangle): # This class Inherit from Rectange class
    def __init__(self, length) -> None:
        super().__init__(length, length)
    
        

#More Example

class Cube(WithSuperSquare):
    def surface_area(self):
        suf_area = super().area() 
        return suf_area * 6

    def volume(self):
        suf_area = super().area()
        return suf_area*self.length



class Triangle:
    def __init__(self,base,height) -> None:
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height

    

# class RightPyramid(Triangle,WithSuperSquare):
#     def __init__(self, base, slant_height) -> None:
#         super().__init__(base, slant_height)
#         self.base=base
#         self.slant_height=slant_height

#     def area(self):
#         base_area= super.area()
#         perimeter = super.perimeter()
#         return 0.5*perimeter*self.slant_height+base_area


class RightPyramid(WithSuperSquare,Triangle):
    def __init__(self, base, slant_height) -> None:
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area= super().area()
        perimeter = super().perimeter()
        return 0.5*perimeter*self.slant_height+base_area
        


# ob=Square(4)
# print(ob.area())

# cubeOb = Cube(4)
# print(cubeOb.surface_area())
        
pyramid = RightPyramid(2,4)
print(pyramid.area())

