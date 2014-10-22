from thing import *


class Computer (Thing):

    def __init__(self, name, loc, desc="Smarter than you."):
        Thing.__init__(self, name, loc, desc)

    def use(self, actor):
        inv = actor.peek_around()
        used = False
        for item in inv:
            if item.is_homework() and not item.done():
                actor.say("AT LAST! {} shall trouble me no more!".format(item.name()))
                item.do()
                used = True

        if not used:
            actor.say("You browse Bookface to see what the friends you don't have are up to.")

class RiccardoComputer (Computer):

    def __init__(self, name, loc, desc="Riccardo's computer."):
        Computer.__init__(self, name, loc, desc)

    def use(self, actor):
        if actor.has_type(Cable):
            actor.say("A cable for my computer! I can finally connect to this projector.")
            # actor.lecture()
            exit()
        else:
            actor.say("I need a cable to connect to the projector.")