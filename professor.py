from player import *
from npc import *
import random
import homework

class Professor (NPC):

	def __init__ (self,name,loc,restlessness,professorial):
			NPC.__init__(self,name,loc,restlessness,100)
			self._professorial = professorial
			Player.clock.register(self.lecture, 4)

	_topics = ['Turing machines',
						 'the lambda calculus',
						 'Godel']

	def lecture (self,time):
		if not self.is_in_limbo():
			if random.randrange(self._professorial) == 0:
					if self.people_around():
							self.location().report(self.name()+' starts lecturing about '+random.choice(self._topics))
					else:
							self.location().report(self.name()+' mutters to himself about '+random.choice(self._topics))

	def accept(self, obj, source):
		if obj.is_mobile_thing():
			if isinstance(obj, homework.Homework):
				self.add_thing(obj)
				self.say('Ah, a homework to be graded! Let\'s see here...')
				if obj.done():
					self.say('Good, good... Excellent...')
					self.say('Mmm, could have used some more comments.')
					self.say('All in all, well done. Top work.')
					obj.give(self,source)
					self.say('Looks like that\'s enough to pass the class. Congrats.')
					exit()
				else:
					self.say('Wait, this homework\'s not even been started!')
					obj.give(self, source)