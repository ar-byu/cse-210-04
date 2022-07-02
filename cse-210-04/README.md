# Greed
"He who is not contented with what he has, would not be contented with what he would like to have."
 ~ Socrates 

## Getting Started
---
Make sure you have Python 3.8 or newer installed, as well as the Raylib module. You can install the Raylib module from a terminal and running this command:
 
```
python3 -m pip install raylib
```
Once you have installed the module and downloaded the files for this game, you can run it from a terminal using the following command (or a variation, if you have it saved into a subfolder):
```
python3 greed
```
You can also run the program from an IDE such as Visual Studio Code. Select the "main" program and press the Run button.

### How to Play
---
You play as the '@' symbol at the bottom of the screen. Use the left and right arrow keys to move back and forth along the screen, collecting gems and avoiding rocks.

There are four kinds of gems, each with a different point value. Rocks subtract a random number of points within the range of 1 and 10.

There is no game over; the game continues until the player closes the window.

## Project Structure
---
I've structured this program like so:
---
The project files and folders are organized as follows:

```
casting             (cast object files for game)
director            (game master file)
services            (keyboard and screen files)
shared              (shared files for positioning and color)
__main__.py         (the main access point for the game)
README.md           (general information)
```
## Required Technologies
---
* Python 3.8.0 or newer
* Raylib Python CFFI 3.7

## Authors
---
Anna Rector, CSE 210 student. lighteternal.lunae@gmail.com, arector2002@gmail.com

_**It is important to note that several of the classes and methods in this project were copied from CSE 210's earlier project, Robot Find Kitten, due to the similarities between both games. However, the bulk of how the game itself is played and runs was written by the author, as Greed is different enough from RFK to warrant many major changes to the functionality.**_