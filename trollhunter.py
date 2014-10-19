from npc import NPC
from troll import Troll
import random
import player


class TrollHunter(NPC):

    def __init__(self, name, loc, efficacy=2):
        super(TrollHunter, self).__init__(name, loc)
        self._efficacy = efficacy
        player.Player.clock.register(self.check_for_trolls, 3)

    def move_and_take_stuff(self, time):
        pass

    def check_for_trolls(self, time):
        if not self.find_troll():
            self.location().report("{} sniffs the air with a wary look before moving on. What a queer fellow.".format(self.name()))
            self.move_somewhere()

    def find_troll(self):
        for item in self.location().contents():
            if isinstance(item, Troll):
                self.say("AHA! A troll! {} leaps into the fray, and narrates his actions in third person!".format(self.name()))
                self.attack(item, random.randint(1, self._efficacy))
                return True
