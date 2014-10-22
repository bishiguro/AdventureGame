from mobile import *


class Homework (MobileThing):

    def __init__(self, name, loc):
        MobileThing.__init__(self, name, loc,takeable=True)
        self._done = False

    def use(self, actor):
        actor.say("What is this, the 20th century?" +
                  " I'll need much more than a pencil" +
                  " and paper for this one.")

    def done(self):
        return self._done

    def do(self):
        if not self._done:
            self._done = True
            self.set_name("{} (done)".format(self.name()))

    def is_homework(self):
        return True
