#Imports classes from other files

from casting.actor import Moveable
from shared.point import Point

class Artifact(Moveable):
    #A non-player-controlled Moveable objects
    def __init__(self, position, symbol, color, point_value):
        #Initializes the artifact's attributes
        super().__init__(position, symbol, color)
        self._point_value = point_value

    def get_point_value(self):
        #Gets the artifact's point value
        return self._point_value
    
    def move_next(self, max_x, max_y):
        #Moves the actor according to its velocity. Wraps the position when it reaches the maximum x or y values
        #Arguments: max_x (maximum x value), max_y (maximum y value)
        x = (self._position.get_x() + self._vector.get_x()) % max_x
        y = (self._position.get_y() + self._vector.get_y())
        if y >= max_y:
            y = max_y
        self._position = Point(x, y)