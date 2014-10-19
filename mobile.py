from thing import *
import person

class MobileThing (Thing):

    def __init__ (self,name,loc,desc=None):
        Thing.__init__(self,name,loc,desc)
        self._original_location = loc

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

        if isinstance(target, person.Person):
            actor.del_thing(self)
            self._location = target
            actor.say('I give {} to {}'.format(self.name(), target.name()))
            target.accept(self,actor)

    def move (self,loc):
        self.location().del_thing(self)
        loc.add_thing(self)
        self._location = loc

    def creation_site (self):
        return self._original_location

    def is_mobile_thing (self):
        return True