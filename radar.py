from mobile import *
from room import *
import person


class Radar (MobileThing):

    def __init__ (self,name,loc):
        MobileThing.__init__(self,name,loc,takeable=True)

    def use (self,actor):
        actor.say('I fiddle with the buttons on ' + self.name());
        for room in Room.getRooms():
        	for item in room.contents():
        		actor.say('I detect {} in {}'.format(item.name(), room.name()))
        		if isinstance(item, person.Person):
        			for p_item in item.contents():
        			 	actor.say('I detect {} with {}'.format(p_item.name(), item.name()))