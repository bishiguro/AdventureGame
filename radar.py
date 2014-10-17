from mobile import *
from room import *


class Radar (MobileThing):

    def __init__ (self,name,loc):
        MobileThing.__init__(self,name,loc)

    def use (self,actor):
        actor.say('I fiddle with the buttons on ' + self.name());
        for room in Room.getRooms():
        	for item in room.contents():
        		disp('I detect ' + item.name + ' in ' + room.name)

        # FIX ME
        #actor.say("Mmm. It looks like it's broken...")