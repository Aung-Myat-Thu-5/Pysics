import math

class Vector2:

    def __init__(self,x : float = 0.0 ,y : float = 0.0):
        self.x = float(x)
        self.y = float(y)

    def __add__ (self,o:Vector2): return Vector2(self.x + o.x, self.y + o.y)
    def __sub__ (self,o:Vector2): return Vector2(self.x - o.x, self.y - o.y) 
    def __mul__ (self,s)        : return Vector2(self.x * s, self.y * s) 
    __rmul__ = __mul__
    def __truediv__ (self,s)    : return Vector2(self.x /s , self.y /s) 
    def __neg__ (self)          : return Vector2(-self.x , - self.y)
    def __repr__ (self)         : return f"Vector2({self.x:.3f},{self.y:.3f})"
    def __eq__ (self,o)         : return self.x == o.x and self.y == o.y
    
    def dot (self,o)            : return ((self.x * o.x) + (self.y * o.y))
    def cross (self,o)          : return ((self.x*o.y) - (self.y*o.x))
    def length_sq(self)         : return (self.dot(self))
    def length(self)            : return math.sqrt(self.length_sq())
    def normalized(self)        :
        l = self.length
        return Vector2(self.x / l , self.y/l) if l > 0 else Vector2()
    def perp(self)              : return Vector2(-self.y,self.x)
