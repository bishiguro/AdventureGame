from thing import *

class MobileThing (Thing):

    def __init__ (self,name,loc):
        Thing.__init__(self,name,loc)
        self._original_location = loc

    def move (self,loc):
        self.location().del_thing(self)
        loc.add_thing(self)
        self._location = loc

    def creation_site (self):
        return self._original_location

    def is_mobile_thing (self):
        return True

