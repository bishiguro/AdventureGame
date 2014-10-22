from thing import *
import person

class MobileThing (Thing):

    def __init__ (self,name,loc,desc="Light enough to take...", takeable=False):
        Thing.__init__(self,name,loc,desc)
        self._original_location = loc
        self._takeable = takeable

    def takeable(self):
        return self._takeable

    def take (self, actor):
        self._location.lose(self, actor)

    def drop (self,actor):
        self.move(actor.location())

    def give (self,actor,target):
        # if isinstance(target, person.Person):
        response = target.accept(self,actor)
        if response:
            actor.say('I give {} to {}'.format(self.name(), target.name()))
            target.say(response)
            self.move(target)

    def move (self,loc):
        self.location().del_thing(self)
        loc.add_thing(self)
        self._location = loc

    def creation_site (self):
        return self._original_location

    def is_mobile_thing (self):
        return True