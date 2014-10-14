from player import *
from npc import *
import random

class Professor (NPC):

			def __init__ (self,name,loc,restlessness,professorial):
					NPC.__init__(self,name,loc,restlessness,100)
					self._professorial = professorial

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
