from vector_math import Vector2

class Body:
    def __init__(self,position : Vector2 , velocity : Vector2 = None  , mass : float = 1.0):
        self.position = position
        self.velocity = velocity if velocity is not None else Vector2()
        self.mass = mass
        self.force = Vector2() #for accumulating forces on the body

    def apply_force(self, force : Vector2):
        self.force = self.force + force

    def integrate(self, dt:float):
        acceleration = self.force * (1/self.mass)
        self.velocity = self.velocity + acceleration * dt
        self.position = self.position + self.velocity * dt
        self.force = Vector2()

body = Body(position = Vector2(0,0))
print(body.position)