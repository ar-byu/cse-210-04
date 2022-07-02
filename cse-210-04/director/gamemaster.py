# GameMaster copied from RFK exercise
from shared.vector import Vector
from casting.artifact import Artifact
from shared.point import Point
from casting.artifact_factory import ArtifactFactory
import random

CELL = 15

class GameMaster:
    #The orchestrator of the game. Director controlls the sequence of play.
    #Attributes: keyboard_service (gets directional input), gameboard (provides game visuals),
    #game_state (initializes the state of the game), artifact_factory (generates artifacts)

    def __init__(self, keyboard_service, gameboard):
        #Constructs a new GameMaster using the specified keyboard and video services
        #Arguments: keyboard_service (an instance of Keyboard), video_service (an instance of GameBoard)
        self._keyboard_service = keyboard_service
        self._gameboard = gameboard
        self._game_state = GameState()
        self._artifact_factory = ArtifactFactory(2,2)
        
    def start_game(self, cast):
        #Starts the game using the given cast and runs the main game loop
        #Arguments: cast (the cast of actors)
        self._gameboard.open_window()
        while self._gameboard.is_window_open():
            self._get_inputs(cast)
            self._apply_gravity(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._gameboard.close_window()

    def _get_inputs(self, cast):
        #Gets directional input from the keyboard and applies it to the player
        #Arguments: cast (the cast of actors)
        player = cast.get_first_actor("players")
        vector = self._keyboard_service.get_direction()
        player.set_vector(vector)

    def _apply_gravity(self, cast):
        #Makes the artifacts move down
        artifacts = cast.get_actors("artifacts")
        for artifact in artifacts:
            artifact.set_vector(Vector(0,15))

    def _do_updates(self, cast):
        #Updates the player's position and resolves collisions with artifacts. Also displays and updates the points via the banner
        #and populates new rows
        #Arguments: cast (the cast of actors)
        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("players")

        max_x = self._gameboard.get_width()
        max_y = self._gameboard.get_height()
        player.move_next(max_x, max_y)

        self._produce_artifacts(cast)
        artifacts = cast.get_actors("artifacts")

        for artifact in artifacts:
            artifact.move_next(max_x, max_y)

        for artifact in artifacts:
            if player.get_position().equals(artifact.get_position()):
                self._game_state.give_points(artifact.get_point_value())
                cast.remove_actor("artifacts", artifact)

        banner.set_text(f"Score: {self._game_state.get_points()}")
        
    def _produce_artifacts(self, cast):
        #Produces new artifacts for a new row
        for cell in range(0, 60):
            artifact = self._artifact_factory.make_artifact(Point(cell * CELL, 0))
            if artifact != None:
                cast.add_actor("artifacts", artifact)
                
    def _do_outputs(self, cast):
        #Draws the actors on the screen
        #Arguments: cast (the cast of actors)
        self._gameboard.clear_buffer()
        actors = cast.get_all_actors()
        self._gameboard.draw_actors(actors)
        self._gameboard.flush_buffer()

class GameState:
    #Keeps track of the points
    def __init__(self):
        self._points = 0

    def get_points(self):
        return self._points

    def give_points(self, point_worth):
        self._points += point_worth