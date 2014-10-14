from person import *
from player import *
import random

class NPC (Person):

    def __init__ (self,name,loc,restlessness,miserly):
        Person.__init__(self,name,loc)
        self._restlessness = restlessness
        self._miserly = miserly
        
    def move_and_take_stuff (self,time):
        if not self.is_in_limbo():
            if random.randrange(self._restlessness) == 0:
                self.move_somewhere()
            if random.randrange(self._miserly) == 0:
                self.take_something()

    def move_somewhere (self):
        exits = self.location().exits()
        if exits:
            dir = random.choice(exits.keys())
            self.go(dir)

    def take_something (self):
        everything = []
        everything.extend(self.stuff_around())
        everything.extend(self.peek_around())
        if everything:
            something = random.choice(everything)
            something.take(self)

    def die (self):
        self.say('SHREEEEEK! I, uh, suddenly feel very faint...')
        Person.die(self)
