class Vector:
    #Keeps track of the direction in which a moveable object is going

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

    def scale(self, factor):
        #Scales and returns the point by a provided factor
        return Vector(self._x * factor, self._y * factor)