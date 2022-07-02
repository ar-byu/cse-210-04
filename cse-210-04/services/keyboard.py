#KeyboardService class imported from RFK exercise

#Imports module and class from elsewhere
import pyray
from shared.vector import Vector

class KeyboardService:
    #Gets keyboard input from the player. Detects player key presses and translates them into a point representing a direction

    def __init__(self, cell_size = 1):
        #Constructs a new Keyboard using the specified cell size
        #Arguments: cell_size
        self._cell_size = cell_size

    def get_direction(self):
        #Gets the selected direction based on the currently pressed keys
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        direction = Vector(dx, dy)
        direction = direction.scale(self._cell_size)

        return direction