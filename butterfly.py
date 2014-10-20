from npc import NPC
import random
import player
from mobile import MobileThing
from wobject import WObject
from butterfly_stages import *
from room import Room

class Butterfly(WObject):

    def __init__(self, name, loc):

        self._location = loc
        self._name = name
        player.Player.clock.register(self.grow, 5)

        self.age = 0
        self.stage_1 = random.randint(5,15)
        self.stage_2 = random.randint(5,15)
        self.stage = Caterpillar(name, loc)

    def location(self):
        return self._location

    def grow(self, time):

        self.age += 1
        loc = self.stage.location()
        # Caterpillar to Cocoon transformation
        if isinstance(self.stage, Caterpillar) and self.age >= self.stage_1: 
            if isinstance(loc, Room):
                loc.report(self.name() + ' starts to spin a cocoon.')
            elif isinstance(loc, Person):
                loc.location().report(self.name() + ' starts to spin a cocoon.')
            
            next_stage = Cocoon(self.name(), loc) 
            self.stage.destroy()
            self.stage = next_stage

        # Cocoon to Butterfly transformation
        if isinstance(self.stage, Cocoon) and self.age >= self.stage_1 + self.stage_2:
            
            if isinstance(self.stage.location(), Room):
                loc.report(self.name() + ' is emerging from the cocoon...')

            elif isinstance(loc, Person):
                loc.location().report(self.name() + ' is emerging from the cocoon...')
                loc.say('Be free, ' + self.name() + '!  I\'ll miss you!')

            next_stage = Papillon(self.name(), loc) 
            self.stage.destroy()
            self.stage = next_stage