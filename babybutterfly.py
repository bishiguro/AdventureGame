import random
import player
from mobile import MobileThing
from papillon import Papillon
from room import Room
from person import Person


class BabyButterfly(MobileThing):

    def __init__(self, name, loc):
        self.state = Caterpillar(self)
        super(BabyButterfly, self).__init__(name, loc, desc=self.state.desc(),takeable=True)
        player.Player.clock.register(self.grow, 5)

    def changeState(self, state):
        if state == Papillon:
            loc = self.location()
            if isinstance(loc, Person):
                loc.say("Be free {}, I'll miss you!".format(self.name()))
                loc = loc.location()
            state(self.name(), loc)
            self.destroy()

        else:
            self.state = state(self)
            self.desc = self.state.desc()

    def desc(self):
        return self.state.desc()

    def grow(self, time):
        self.state.grow()


class ButterflyState:

    def __init__(self, msg, desc, next_stage, manager):
        self._manager = manager
        self._next_stage = next_stage
        self._desc = desc
        self._message = msg
        self._grow_time = random.randint(5, 15)

    def desc(self):
        return self._desc

    def grow(self):
        self._grow_time -= 1
        if self._grow_time <= 0:
            self.report("{} {}".format(self._manager.name(), self._message))
            self._manager.changeState(self._next_stage)

    def report(self, notification):
        self._manager.location().report(notification)


class Caterpillar(ButterflyState):

    def __init__(self, manager):
        msg = "begins to spin a cocoon"
        desc = "A fuzzy caterpillar."
        next_stage = Cocoon
        super(Caterpillar, self).__init__(msg, desc, next_stage, manager)


class Cocoon(ButterflyState):

    def __init__(self, manager):
        msg = "is emerging from the cocoon!"
        desc = "A small, brown cocoon."
        next_stage = Papillon
        super(Cocoon, self).__init__(msg, desc, next_stage, manager)
