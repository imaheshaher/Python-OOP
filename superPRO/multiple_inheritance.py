from .super import *
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
        super().__init__(base, slant_height)
        self.base=base
        self.slant_height=slant_height

    def area(self):
        base_area= super.area()
        perimeter = 1
        return 0.5*perimeter*self.slant_height+base_area
        
pyramid = RightPyramid(2, 4)
print(pyramid.area())
