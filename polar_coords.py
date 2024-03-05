import math

class Polar:
    def __init__(self,radius,angle):
        self.radius = radius
        self.angle = angle

    def __repr__(self):
        return f"{self.radius} {self.angle}"
    
    def __add__(self,other):
        x1 = self.radius * math.cos(math.radians(self.angle))
        y1 = self.radius * math.sin(math.radians(self.angle))
        x2 = other.radius * math.cos(math.radians(other.angle))
        y2 = other.radius * math.sin(math.radians(other.angle))

        x_sum = x1 + x2
        y_sum = y1 + y2

        result_radius = math.sqrt(x_sum**2 + y_sum**2)
        result_angle = math.degrees(math.atan2(y_sum, x_sum))

        return Polar(result_radius, result_angle)
    
polar1 = Polar(3, 45)
polar2 = Polar(2, 30)


result = polar1 + polar2
print(result) 