from wobject import *
from player import *

class Thing (WObject):

    def __init__ (self,name,loc,desc=None):
        WObject.__init__(self,name)
        self._location = loc
        loc.add_thing(self)
        self.desc = desc

    def use (self,actor):
        actor.say('I try to use '+self.name()+' but nothing happens')

    def take (self,actor):
        actor.add_thing(self)
        self._location.del_thing(self)
        self._location = actor

    def drop (self,actor):
        if actor.have_thing(self):
            actor.del_thing(self)
            actor._location.add_thing(self)
            self._location = actor.location()
        else:
            actor.say(actor.name(),'is not carrying',self.name())

    def give (self,actor,target):
        actor.del_thing(self)
        target.add_thing(self)
        self._location = target
        actor.say('I give {} to {}'.format(self.name(), target.name()))

        target.accept(self, actor)

    def location (self):
        return self._location
        
    def is_in_limbo (self):
        return self.location() is None

    def destroy (self):
        self._location.del_thing(self)
        self._location = None

    def is_thing (self):
        return True

    def look(self):
        if self.desc:
            output = self.desc
        else:
            output = "Your run-of-the-mill " + self.name() + "."

        self._location.report(output)
