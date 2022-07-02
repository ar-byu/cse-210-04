# The Cast class was copied from the RFK exercise earlier in the week

class Cast:
    #A collection of actors. Cast keeps track of each actor, including adding, removing, and getting by group name

    def __init__(self):
        #Constructs a new actor
        self._actors = {}
        
    def add_actor(self, group, actor):
        #Adds an actor to the given group
        #Arguments: group (the name of the group), actor (the actor to add)
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        #Gets and returns the actors in the given group
        #Arguments: group (the name of the group)
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_all_actors(self):
        #Gets all of the actors in the cast
        #Returns a list of all actors
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_first_actor(self, group):
        #Gets and returns the first actor in the given group
        #Arguments: group (the name of the group)
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result

    def remove_actor(self, group, actor):
        #Removes an actor from the given group
        #Arguments: group (the name of the group), actor (the actor to remove)
        if group in self._actors:
            self._actors[group].remove(actor)