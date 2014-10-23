from mobile import *
from cable import Cable
import player

class Person (MobileThing):    # Container...

    def __init__ (self,name,loc,desc="A person, you think."):
        MobileThing.__init__(self,name,loc,desc)
        self._max_health = 3
        self._health = self._max_health
        self._contents = []

    def contents (self):
        return self._contents

    def have_thing (self,t):
        for c in self.contents():
            if c is t:
                return True
        return False

    def add_thing (self,t):
        if isinstance(t, MobileThing):
            self._contents.append(t)
        else: self.say("I can't pick up {}.".format(t.name()))

    def del_thing (self,t):
        self._contents = [x for x in self._contents if x is not t]

    def health (self):
        return self._health

    def reset_health (self):
        self._health = self._maxHealth

    def say (self,msg):
        self.report(self.name()+' says -- '+msg)

    def report(self, msg):
        self._location.report(msg)

    def have_fit (self):
        self.say('Yaaaaah! I am upset!')

    def people_around (self):
        return [x for x in self.location().contents()
                    if x.is_person() and x is not self]

    def stuff_around (self):
        return [x for x in self.location().contents() if not x.is_person()]

    def possessions(self):
        p = []
        for x in self.location().contents():
            if x.is_person() and not x == player.Player.me:
                p.extend(x.contents())
        return p

    def peek_around (self):
        """
        Returns everything at a loction even if it is
        in another person's inventory.
        """

        everything = self.stuff_around()
        for person in self.people_around():
            everything.extend(person.contents())

        return everything

    def lose (self,t,loseto):
        self.say('I lose ' + t.name())
        self.have_fit()
        t.move(loseto)
    
    def go (self,direction):
        loc = self.location()
        exits = loc.exits()
        if direction in exits:
            t = exits[direction]
            self.leave_room()
            loc.report(self.name()+' moves from '+ loc.name()+' to '+t.name())
            self.move(t)
            self.enter_room()
            return True
        else:
            print('No exit in direction', direction)
            return False


    def suffer (self,hits):
        self.say('Ouch! '+str(hits)+' hits is more than I want!')
        self._health -= hits
        if (self.health() < 0):
            self.die()
        else:
            self.say('My health is now '+str(self.health()))

    def die (self):
        self.location().broadcast('An earth-shattering, soul-piercing scream is heard...')

        for item in self.contents():
            item.drop(self)

        if player.Player.god_mode:
            print("{} has died.".format(self.name()))
        self.destroy()

    def enter_room (self):
        people = self.people_around()
        if people:
            self.say('Hi ' + ', '.join([x.name() for x in people]))

        if self.has_cable():
            for person in people:
                person.cableNotify(self)

    def has_cable(self):
        for c in self._contents:
            if isinstance(c, Cable):
                return True

        return False

    def cableNotify(self, target):
        pass

    def leave_room (self):
        pass   # do nothing to reduce verbiage

    def take (self, actor):
        actor.say('I am not strong enough to just take ' + self.name())

    def accept (self,obj,source):
        return 'Thanks, {}'.format(source.name())

    def is_person (self):
        return True
