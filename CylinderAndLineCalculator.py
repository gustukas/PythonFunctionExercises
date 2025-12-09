class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        d = (((self.coor2[0]-self.coor1[0])**2 + (self.coor2[1]-self.coor1[1])**2)**0.5)
        return d
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        m = (y2-y1)/(x2-x1)
        return m


coordinate1 = (3,2)
coordinate2 = (8,10)

line1 = Line(coordinate1,coordinate2)

print(line1.distance())
print(line1.slope())



class Cylinder:
    
    pi = 3.14

    def __init__(self,height,radius):
        self.height = height
        self.radius = radius
        
    def volume(self):
        h = self.height
        r = self.radius
        pi = self.pi
        V = (pi)*(r**2)*(h)
        return V
    
    def surface_area(self):
        h = self.height
        r = self.radius
        pi = self.pi
        A = (2*pi*r*h)+(2*pi*(r**2))
        return A

c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())