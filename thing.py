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
        actor.say('I try to take '+self.name()+" but can't")

    def drop (self,actor):
        print(actor.name(),'is not carrying',self.name())

    def give (self,actor,target):
        print(actor.name(),'is not carrying',self.name())

    def location (self):
        return self._location
        
    def is_in_limbo (self):
        return self.location() is None

    def destroy (self):
        self._location.del_thing(self)
        self._location = None

    def is_thing (self):
        return True

    def examine(self):
        if self.desc:
            output = self.desc
        else:
            output = "Your run-of-the-mill " + self.name() + "."

        self._location.report(output)


class VerboseThing(Thing):
    def __init__(self, name, loc, desc):
        super(VerboseThing, self).__init__(name, loc)
        self.desc = desc

