class Point:
    #Point holds and provides information about itself.
    
    def __init__(self, x, y):
        #Constructs a new Point using a specified value
        #Arguments: x (given X position), y (given Y position)
        self._x = x
        self._y = y

    def add(self, other):
        #Gets and returns a new point that is the sum of this and the given one.
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        #Checks whether or not the current point is equal to the given one
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        #Gets and returns the horizontal distance
        return self._x

    def get_y(self):
        #Gets and returns the vertical distance
        return self._y

    def scale(self, factor):
        #Scales and returns the point by a provided factor
        return Point(self._x * factor, self._y * factor)