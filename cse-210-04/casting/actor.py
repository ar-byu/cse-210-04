from shared.point import Point
from shared.vector import Vector

# Much of the code here pulled from RFK

class Actor:
    #A visible object that is important to the game.
    # This class keeps track of the object's appearance, position, and velocity if applicable.
    #Attributes: text, font_size, color, position

    def __init__(self, position, text, color):
        #Constructs a new Actor
        self._text = text
        self._font_size = 15
        self._color = color
        self._position = position

    def get_color(self):
        #Gets and returns the actor's color
        return self._color

    def get_font_size(self):
        #Gets and returns actor's font size
        return self._font_size

    def get_position(self):
        #Gets and returns actor's position
        return self._position

    def get_text(self):
        #Gets and returns actor's text
        return self._text

    def set_color(self, color):
        #Updates color to the given one
        self._color = color

    def set_position(self, position):
        #Updates position to the given one
        self._position = position
    
    def set_font_size(self, font_size):
        #Updates font size to the given one
        self._font_size = font_size
    
    def set_text(self, text):
        #Updates text to the given value
        self._text = text

class Moveable(Actor):
    #A descendant of Actor. Moveables are the objects that actually move around on the screen.

    def __init__(self, position, symbol, color):
        #Initializes the Moveable
        super().__init__(position, symbol, color)
        self._vector = Vector(0,0)

    def get_vector(self):
        #Gets and returns actor's vector
        return self._vector

    def set_vector(self, vector):
        #Updates velocity to the given value
        self._vector = vector

    def move_next(self, max_x, max_y):
        #Moves the actor according to its velocity. Wraps the position when it reaches the maximum x or y values
        #Arguments: max_x (maximum x value), max_y (maximum y value)
        x = (self._position.get_x() + self._vector.get_x()) % max_x
        y = (self._position.get_y() + self._vector.get_y()) % max_y
        self._position = Point(x, y)
        