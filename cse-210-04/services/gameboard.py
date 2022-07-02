# GameBoard class copied from RFK exercise

import pyray

class GameBoard:
    #Displays the board

    def __init__(self, caption, width, height, cell_size, frame_rate, debug = False):
        #Constructs a new board using the specified debug mode
        #Arguments: debug (sets whether or not to use debug mode)
        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug

    def close_window(self):
        #Closes the window and releases all computing resources.
        pyray.close_window()

    def clear_buffer(self):
        #Clears the buffer to prepare for the next rendering.
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    def draw_actor(self, actor):
        #Draws the given actor's text on the screen
        #Arguments: actor (the actor to draw)
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()
        pyray.draw_text(text, x, y, font_size, color)
        
    def draw_actors(self, actors):
        #Draws the text for the given list of actors
        #Arguments: actors (a list of actors to draw)
        for actor in actors:
            self.draw_actor(actor)
        
    
    def flush_buffer(self):
        #Copies content of the buffer to the screen.
        pyray.end_drawing()

    def get_cell_size(self):
        #Gets and returns the video screen's cell size
        return self._cell_size

    def get_height(self):
        #Gets and returns the screen's height
        return self._height

    def get_width(self):
        #Gets and returns the screen's width
        return self._width

    def is_window_open(self):
        #Checks whether the window was closed by the user
        return not pyray.window_should_close()

    def open_window(self):
        #Opens a new window
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)

    def _draw_grid(self):
        #Draws a grid on the screen
        for y in range(0, self._height, self._cell_size):
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)
        for x in range(0, self._width, self._cell_size):
            pyray.draw_line(x, 0, x, self._height, pyray.GRAY)