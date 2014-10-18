from thing import *


class Computer (Thing):

    def __init__(self, name, loc, desc="Smarter than you."):
        Thing.__init__(self, name, loc, desc)

    def use(self, actor):
        inv = actor.peek_around()
        for item in inv:
            if item.is_homework() and not item.done():
                actor.say("AT LAST! {} shall trouble me no more!".format(item.name()))
                item.do()
