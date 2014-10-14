import random
from npc import *

class Troll (NPC):

    def __init__ (self,name,loc,restlessness,hunger):
        NPC.__init__(self,name,loc,restlessness,10)
        self._hunger = hunger

    def eat_people (self,time):
      if not self.is_in_limbo():
        if random.randrange(self._hunger) == 0:
            people = self.people_around()
            if people:
                victim = random.choice(people)
                self.location().report(self.name() + ' takes a bite out of ' + victim.name())
                victim.suffer(random.randint(1,3))
            else:
                self.location().report(self.name() + "'s belly rumbles")

