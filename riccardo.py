from person import *
from clock import *

import sys, random
from player import Player

class Riccardo (Player):

    def __init__ (self,name,loc):
        Player.__init__(self,name,loc)

    _topics = ['Turing machines',
                'the lambda calculus',
                'Godel']

    def lecture (self):
        if self.people_around():
                self.location().report(self.name()+' starts lecturing about '+random.choice(self._topics))
        else:
                self.location().report(self.name()+' mutters to himself about '+random.choice(self._topics))

    def accept(self, obj, source):
        pass