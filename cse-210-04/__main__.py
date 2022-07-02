#Imports several modules and classes

import os
import pyray

from casting.actor import Actor, Moveable
from casting.artifact import Artifact
from casting.cast import Cast

from director.gamemaster import GameMaster

from services.keyboard import KeyboardService
from services.gameboard import GameBoard

from shared.color import Color
from shared.point import Point


#Initializes several variables

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
CAPTION = "Greed"
WHITE = Color(255, 255, 255)

def main():
    #Generates a cast, a banner, a player, keyboard service, board, game master, and calls the "start_game" method from the GameMaster
    cast = Cast()
    banner = Actor(Point(CELL_SIZE,0), "Score: 0", WHITE)
    cast.add_actor("banners", banner)

    player = Moveable(Point(int(MAX_X/2), MAX_Y - CELL_SIZE), "@", WHITE)
    cast.add_actor("players", player)

    keyboard_service = KeyboardService(CELL_SIZE)
    gameboard = GameBoard(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = GameMaster(keyboard_service, gameboard)
    director.start_game(cast)



if __name__ == "__main__":
    #Runs the game
    main()