class Color:
    #Assigns color to the actors. Holds and provides information about itself.
    
    def __init__(self, red, green, blue, alpha = 255):
        #Constructs a new color using the specified red, green, blue, and alpha values. Alpha is set to 255 by default
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    def to_tuple(self):
        #Gets and returns the color as a tuple
        return (self._red, self._green, self._blue, self._alpha)