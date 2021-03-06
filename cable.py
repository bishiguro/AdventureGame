from mobile import *
from computer import *
import random
import person

class Cable (MobileThing):

	def __init__ (self,name,loc):
		self.desc = "The elusive {} cable".format(name)
		MobileThing.__init__(self,name,loc,desc=self.desc,takeable=True)

	def use(self, actor):
		if actor._location.has_type(RiccardoComputer):
			actor.say("I finally have the correct cable! Time to finish this lecture.")
			actor.lecture()
			actor._location.report('')
			exit()
		elif actor._location.has_type(Computer):
			actor.say("This is not MY computer. Let's head back to class.")
		else:
			actor.say("I don't see a computer in this room.")