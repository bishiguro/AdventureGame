
import random

from room import *
from verbs import *
from player import *
from npc import *
from radar import *
from troll import *
from professor import *
from homework import *
from computer import *
from badninja import *
from trollhunter import TrollHunter
from babybutterfly import BabyButterfly

REVERSE = {
    'north' : 'south',
    'east' : 'west',
    'south' : 'north',
    'west' : 'east',
    'up' : 'down',
    'down' : 'up'
}


# add an exit in 'fr' toward 'to' in direction 'dir'
def connect (fr,dir,to):
    fr.exits()[dir] = to

# add an exit in 'fr' toward 'to' in direction 'dir'
# and an exit the other way, in 'to' toward 'fr' in the reverse direction
def biconnect (fr,dir,to):
    connect(fr,dir,to)
    connect(to,REVERSE[dir],fr)



def create_world ():

    mh353 = Room('Riccardo Office')
    mh3rd = Room('Milas Hall Third Floor')
    mh2nd = Room('Milas Hall Second Floor')
    mh1st = Room('Milas Hall First Floor')
    oval = Room('Oval')
    ac1st = Room('Academic Center First Floor')
    ac113 = Room('Academic Center 113')
    cc1st = Room('Campus Center First Floor', '')
    # West Hall
    westh = Room('West Hall')
    wh1l = Room('West Hall 1st Floor Lounge', 'The closet door hangs ajar, and a delicious aroma wafts from the North wing.')
    wh2l = Room('West Hall 2nd Floor Lounge')
    wh3l = Room('West Hall 3rd Floor Lounge')
    wh4l = Room('West Hall 4th Floor Lounge')
    nerf = Room('The Armory','Nerf weaponry and foam swords line the shelves.')
    # East Hall
    easth = Room('East Hall')
    eh1l = Room('East Hall 1st Floor Lounge')
    eh2l = Room('East Hall 2nd Floor Lounge')
    eh3l = Room('East Hall 3rd Floor Lounge')
    eh4l = Room('East Hall 4th Floor Lounge')
    # The Unknown
    babson = Room('Babson College')
    shuttle = Room('BOW Shuttle')
    wels = Room('Wellesley College')

    biconnect(oval, 'west',  ac1st)
    biconnect(ac1st, 'north',  ac113)
    biconnect(mh353, 'east',  mh3rd)
    biconnect(mh3rd, 'down',  mh2nd)
    biconnect(mh2nd, 'down',  mh1st)
    biconnect(mh1st, 'north',  oval)
    biconnect(oval, 'east',  cc1st)
    # West Hall
    biconnect(cc1st, 'east',  westh)
    biconnect(wh1l, 'east', nerf)
    biconnect(westh, 'north', wh1l)
    biconnect(westh, 'up', wh2l)
    biconnect(wh2l, 'up', wh3l)
    biconnect(wh3l, 'up', wh4l)
    # East Hall
    biconnect(westh, 'east',  easth)
    biconnect(easth, 'north', eh1l)
    biconnect(easth, 'up', eh2l)
    biconnect(eh2l, 'up', eh3l)
    biconnect(eh3l, 'up', eh4l)
    # The Unknown
    biconnect(oval, 'north',  babson)
    biconnect(shuttle, 'east', babson)
    biconnect(shuttle, 'west', wels)
    biconnect(shuttle, 'north', easth)


    # The player is the first 'thing' that has to be created

    Player('Blubbering-Fool', oval)

    Radar('handy radar', mh353)
    Thing('blackboard', ac113)
    Thing('lovely-trees', oval, "Just enough above you to huff haugtily in the wind as you approach.")
    MobileThing('cs-book', oval)
    MobileThing('math-book', oval, 'Just say no.')
    Computer('hal-9000', ac113, "I can't let you do that, Riccardo.")
    Computer('johnny-5', easth, 'Inpuuuuuuuuuut!')

    # Better things.
    Thing('adequate-trees', oval, "The kind of trees you hang out with, but don't really want to have over for family dinner.")
    Thing('subpar-trees', oval, "A disappointment to look upon. Truly.")
    MobileThing('maverick', nerf, "A steadfast sidearm, reknowned across the west (hall).")
    MobileThing('modded longshot', nerf, "The pinnicle of foam-based warfare.")
    MobileThing('vulcan', nerf, "Compensation for those for whom compensation has lost its original luster.")
    MobileThing('Joe, grandfather of the unicorns', wh2l, "Joe gazes languidly out from the laquered frame, " +
                "with the knowledge that comes only from millenia of strife.")
    MobileThing('gitar', wh3l, 'Your eyes glaze over for a second as you picture stage lights and topless girls.' +
                'You shake yourself back to reality with difficulty.')
    Computer('the phoenix box', wh3l, "The computer other computers wish they could be. Besides, re-images are basically beauty sleep.")
    Computer('space sphere', ac1st, "Wanna go to space! Space. Space. Space. Wanna go to space.")

    Professor('Riccardo', mh353, random.randint(1, 5), 2)

    homeworks = ['hw-1',
                 'hw-2',
                 'hw-3',
                 'hw-4',
                 'hw-5',
                 'hw-6']

    for homework in homeworks:
        Homework(homework,
                 random.choice(Room.rooms))

    students = ['Frankie Freshman',
                'Joe Junior',
                'Sophie Sophomore',
                'Cedric Senior']

    for student in students:
        NPC(student,
            random.choice(Room.rooms),
            random.randint(1, 5),
            random.randint(1, 5))

    trolls = ['Polyphemus',
              'Gollum',
              'Internet-Troll',
              'Alternate-Ricardo']

    for troll in trolls:
      Troll(troll,
            random.choice(Room.rooms),
            restlessness=random.randint(1, 3),
            hunger=random.randint(1, 3))

    troll_hunters = ['Mister Piggy',
                      'Angel']

    for troll_hunter in troll_hunters:
        TrollHunter(troll_hunter,
            random.choice(Room.rooms),
            efficacy=random.randint(1, 4))

    bad_ninjas = ['Trogdor']

    for ninja in bad_ninjas:
        BadNinja(ninja, 
            mh353, 
            random.randint(1,3),
            random.randint(1,3))

    butterflies = ['Marie-Sylvie', 'Sylvester', 'Silas', 'Puck', 'Aoife']
    for butterfly in butterflies:
        BabyButterfly(butterfly, random.choice(Room.rooms))

VERBS = {}



VERBS = {
    'quit' : Quit(),
    'look' : Look(),
    'wait' : Wait(),
    'inv' : Inventory(),
    'take' : Take(),
    'drop' : Drop(),
    'give' : Give(),
    'god'  : God(),
    'use'  : Use(),
    'north' : Direction('north'),
    'south' : Direction('south'),
    'east' : Direction('east'),
    'west' : Direction('west'),
    'up'   : Direction('up'),
    'down' : Direction('down')
}

def dispVerbs():
    print("Available Commands:")
    for verb in VERBS:
        print("--{}".format(verb))


def print_tick_action (t):
    Player.me.location().report('The clock ticks '+str(t))


def read_player_input ():
    while True:
        response = input('\nWhat is thy bidding? ')
        if len(response)>0:
            return response.split()


SAME_ROUND = 1
NEXT_ROUND = 2  
  
def main ():
    
    print('Olinland, version 1.4 (Fall 2014)\n')


    # Create the world
    create_world()
    Player.clock.register(print_tick_action, 0)
    Player.me.look_around()


    while True:
        response = read_player_input ()
        print
        if response[0] == 'help': dispVerbs()
        elif response[0] in sorted(VERBS):
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                print("\n\n")
                Player.clock.tick()
                Player.me.look_around()
        else:
            print('What??')


if __name__ == '__main__':
    main()
