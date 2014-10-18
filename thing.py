from wobject import *
from player import *

class Thing (WObject):

    def __init__ (self,name,loc,desc=None):
        WObject.__init__(self,name)
        self._location = loc
        loc.add_thing(self)
        self.desc = desc

    def take (self,actor):
        actor.say("I can't take that I'm afraid.")

    def drop (self,actor):
        actor.say("I don't have that in my inventory.")

    def give (self,actor,target):
        actor.say("I can't give something I don't have!")

    def use (self,actor):
        actor.say('I try to use '+self.name()+' but nothing happens')

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
