class point(object):
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        
    def __str__(self):
        return("<" + str(self.x) + "," + str(self.y) + ">")
        
    def distance(self, other):
        
        xs = (self.x - other.x) ** 2
        ys = (self.y - other.y) ** 2
        
        return((xs + ys) ** 0.5)
        
c = point(3,4)
origin = point(0,0)

d = point.distance(c, origin)
e = c.distance(origin)

print("d =", d, "e =", e)
        

class fraction:
    def __init__(self, zähler, nenner):
        self.zähler = zähler
        self.nenner = nenner 
        
    def __str__(self):
        return(str(self.zähler) + "/" + str(self.nenner) + " gekürzt: " + str(self.zähler / self.nenner))
        
    def __add__(self, other):
        top = other.nenner * self.zähler + self.nenner * other.zähler
        bottom = self.nenner * other.nenner
        return(fraction(top, bottom))
        
    def __sub__(self, other):
        top = other.nenner * self.zähler - self.nenner * other.zähler
        bottom = self.nenner * other.nenner
        return fraction(top, bottom)
        
drittel = fraction(1,3)
VierAchtel = fraction(4, 8)

print(drittel - VierAchtel)
