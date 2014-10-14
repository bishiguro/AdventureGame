from mobile import *


class Homework (MobileThing):

    def __init__ (self,name,loc):
        MobileThing.__init__(self,name,loc)

    def is_homework (self):
        return True

    # FIX ME
