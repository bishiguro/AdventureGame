from player import *
from npc import *
import random
import homework
import person

class BadNinja (NPC):

	def __init__ (self,name,loc,restlessness,professorial):
			NPC.__init__(self,name,loc,restlessness,100)
			Player.clock.register(self.take_something, 4)

	def take_something(self, *args):
		for person in self.people_around():
			for item in person.contents():
				if isinstance(item, homework.Homework):
					if item.done():
						self.say('Aha! What\'s this! A completed homework? Let me look at it.')
						item.take(self)
						self.say('I take {} from {}'.format(item.name(), person.name()))
						self.say('No, no, no! It\'s all wrong, WRONG!')
						self.say('Burn, baby, burn!')
						item.destroy()