from person import *
from clock import *

import sys

class Player (Person):

    # static field representing the player
    me = None
    # static field recording god_mode
    god_mode = False
    # static field representing the clock
    clock = Clock(0)

    def __init__ (self,name,loc):
        Person.__init__(self,name,loc)
        Player.me = self

    # Grab any kind of thing from player's location, 
    # given its name.  The thing may be in the possession of
    # the place, or in the possession of a person at the place.

    def thing_named (self,name):
        everything = self.peek_around()
        everything.extend(self.contents())
        everything.extend(self.people_around())
        for x in everything:
            if x.name() == name:
                return x

    def look_around (self):
        def names (lst):
            return ', '.join([x.name() for x in lst])

        loc = self.location()
        desc = loc.description()
        exits = loc.exits()
        people = self.people_around()
        all_stuff = self.stuff_around()
        possessions = self.possessions()

        print('------------------------------------------------------------')
        print('You are in', loc.name())
        if desc:
            print(desc)

        if all_stuff:
            print('You see:', names(all_stuff))

        if people:
            print('You see:', names(people))

        if possessions:
            print('People have:', names(possessions))

        if exits:
            print('Exits:', ', '.join([x for x in exits]))
        else:
            print('There are no exits')


    def die (self):
        self.say('I am slain!')
        Person.die(self)
        print('This game for you is now over...')
        sys.exit(0)