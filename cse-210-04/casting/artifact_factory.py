#Imports classes and Random module

from casting.artifact import Artifact
from shared.color import Color
import random

class ArtifactFactory():
    #Initializes the percentages of falling objects
    def __init__(self, gem_percentage, rock_percentage):
        self._gem_percentage = 2
        self._rock_percentage = 2
    
    def make_artifact(self, point):
        #Creates an artifact based on a random number. If the number is less than or equal to gem_percentage, the artifact is a gem.
        #If the number is less than or equal to gem_percentage + rock_percentage, the artifact is a rock.
        #Otherwise, the space is empty
        number = random.randint(1, 100)
        if number <= self._gem_percentage:
            return self._gem(point)
        elif number <= self._gem_percentage + self._rock_percentage:
            return self._rock(point)
        return None

    def _gem(self, point):
        #Picks a random gem color and assigns it the appropriate values
        colors = [Color(243,97,173), Color(97,208,243), Color(97,243,129), Color(243,97,133)]
        color = random.choice(colors)
        if color == colors[0]:
            return Artifact(point, "*", color, 1)
        elif color == colors[1]:
            return Artifact(point, "o", color, 2)
        elif color == colors[2]:
            return Artifact(point, "A", color, 3)
        else:
            return Artifact(point, "8", color, 5)

    def _rock(self, point):
        #Assigns a rock color and a random point value
        color = Color(149,69,53)
        shape = "O"
        point_value = random.randint(-10, -1)
        return Artifact(point, shape, color, point_value)
