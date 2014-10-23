import random
from npc import *
from player import Player

class Troll (NPC):

    def __init__(self, name, loc, desc="Look out, it bites!", restlessness=3, hunger=10):
        super(Troll, self).__init__(name,loc,desc,restlessness)
        self._hunger = hunger
        Player.clock.register(self.eat_people, 3)

    def eat_people(self, time):
      if not self.is_in_limbo():
        if random.randrange(self._hunger) == 0:
            people = self.people_around()
            if people:
                victim = random.choice(people)
                self.location().report(self.name() + ' takes a bite out of ' + victim.name())
                victim.suffer(random.randint(1, 3))
            else:
                self.location().report(self.name() + "'s belly rumbles")
