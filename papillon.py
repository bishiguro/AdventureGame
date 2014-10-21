from npc import *
from mobile import *
from player import *
from room import *
from person import *
import random

class Papillon (NPC):

	def __init__ (self,name,loc):
		NPC.__init__(self,name,loc)
		self.max_health = 1
		self.colors = ['blue', 'purple', 'orange and black', 'blue and black', 'bright orange']
		self.desc = "A lovely " + random.choice(self.colors) + " butterfly."

	def take(self, actor):
		actor.say('I try but fail miserably at catching ' + self.name())

	def move_somewhere (self):
		loc = self.location()
		if isinstance(loc, Person):
			loc.location().report(self.name()+' lifts off of ' + loc.name() + '\'s hand.')
			self.move(loc.location())
		else:
			exits = loc.exits()
			if exits:
				dir = random.choice(list(exits.keys()))
				self.go(dir)

	def go (self,direction):
		loc = self.location()
		exits = loc.exits()
		if direction in exits:
			t = exits[direction]
			loc.report(self.name()+' flies from '+ loc.name()+' to '+t.name())
			self.move(t)
			return True
		else:
			print('No exit in direction', direction)
			return False