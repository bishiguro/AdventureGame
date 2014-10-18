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
