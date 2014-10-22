
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
from cable import Cable
from riccardo import Riccardo
from student import Student

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
    ac2nd = Room('Academic Center Second Floor', 'A series of charcoal drawings line the north wall.')
    acdesign = Room('Academic Center Design Studio', 'Colorful post-it notes and snapped Delrin pieces are strewn over the tables.')
    ac3rd = Room('Academic Center Third Floor')
    acdance = Room('Academic Center Third Floor Endcap')
    ac4th = Room('Academic Center Fourth Floor')
    aclab = Room('Academic Center Biology Lab')

    cc1st = Room('Campus Center First Floor', '')
    # West Hall
    westh = Room('West Hall')
    wh1l = Room('West Hall 1st Floor Lounge', 'The closet door hangs ajar, and a delicious aroma wafts from the North wing.')
    wh2l = Room('West Hall 2nd Floor Lounge')
    wh3l = Room('West Hall 3rd Floor Lounge')
    wh4l = Room('West Hall 4th Floor Lounge')
    nerf = Room('The Armory','Nerf weaponry and foam swords line the shelves.')

    stairsw1 = Room("The Anti-Social Staircase","For when you'd rather be alone.")
    stairsw2 = Room("The Anti-Social Staircase", "For when you'd rather be alone.")
    stairsw3 = Room("The Anti-Social Staircase", "For when you'd rather be alone.")
    stairsw4 = Room("The Anti-Social Staircase", "For when you'd rather be alone.")

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
    greatlawn = Room('The Great Lawn', 'A green expanse of sunshine and happiness.')
    parcelb = Room('Parcel B', 'The brilliant colors and peaceful quiet lure you into a meditative state.')
    bajatrack = Room('Baja Track')
    trebuchet = Room('Trebuchet')

    biconnect(oval, 'west',  ac1st)

    biconnect(ac1st, 'north',  ac113)
    biconnect(ac1st, 'up', ac2nd)
    biconnect(ac2nd, 'up', ac3rd)
    biconnect(ac2nd, 'north', acdesign)
    biconnect(ac3rd, 'up', ac4th)
    biconnect(ac3rd, 'west', acdance)
    biconnect(ac4th, 'west', aclab)

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
    biconnect(greatlawn, 'north', westh)
    biconnect(greatlawn, 'south', parcelb)
    biconnect(parcelb, 'south', bajatrack)
    biconnect(bajatrack, 'south', trebuchet)

    # Anti-Social Elevator
    biconnect(wh1l, 'west', stairsw1)
    biconnect(stairsw1, 'up', stairsw2)
    biconnect(wh2l, 'west', stairsw2)
    biconnect(stairsw2, 'up', stairsw3)
    biconnect(wh3l, 'west', stairsw3)
    biconnect(stairsw3, 'up', stairsw4)
    biconnect(wh4l, 'west', stairsw4)

    # The player is the first 'thing' that has to be created

    #Player('Blubbering-Fool', oval)
    Riccardo('Riccardo', ac113)
    Radar('handy radar', mh353)
    Thing('blackboard', ac113)
    Thing('lovely-trees', oval, "Just enough above you to huff haugtily in the wind as you approach.")
    MobileThing('cs-book', oval)
    MobileThing('math-book', oval, 'Just say no.')
    Computer('hal-9000', wh2l, "I can't let you do that, Riccardo.")
    Computer('johnny-5', easth, 'Inpuuuuuuuuuut!')
    RiccardoComputer('The Mainframe', ac113, 'If only you had a cable...')

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

    homeworks = ['hw-1',
                 'hw-2',
                 'hw-3',
                 'hw-4',
                 'hw-5',
                 'hw-6']

    for homework in homeworks:
        Homework(homework,
                 random.choice(Room.rooms))

    cypress = Student("Cypress", random.choice(Room.rooms))  
    bonbon = Student("Bonskilaylay", random.choice(Room.rooms))
    nick = Student("Nicholas", random.choice(Room.rooms))
    shrinidhi = Student("Shrinidhi", random.choice(Room.rooms))
    zach = Student("Zach", random.choice(Room.rooms))
    greg = Student("Gregleston", ac113)
    haley = Student("Haley", random.choice(Room.rooms))
    chelsea = Student("Chelsea", random.choice(Room.rooms))
    philip = Student("Philip", random.choice(Room.rooms))
    alex = Student("Alex", random.choice(Room.rooms))
    jazmin = Student("Jazmin", random.choice(Room.rooms))
    radmer = Student("Radmer", random.choice(Room.rooms))
    brendan = Student("Brendan", random.choice(Room.rooms))
    tom = Student("Tom", random.choice(Room.rooms))
    allison = Student("Allison", random.choice(Room.rooms))
    jack = Student("Jack", random.choice(Room.rooms))
    ben = Student("Ben", random.choice(Room.rooms))

    trolls = ['Polyphemus',
              'Gollum',
              'Internet-Troll',
              'Alternate-Riccardo']

    for troll in trolls:
      Troll(troll,
            random.choice(Room.rooms),
            random.randint(1, 3),
            random.randint(1, 3))

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

    butterflies = ['Marie-Sylvie', 'Sylvester', 'Puck', 'Aoife']

    for butterfly in butterflies:
        BabyButterfly(butterfly, random.choice(Room.rooms))

    cable_types = ['HDMI', 'VGA', 'DVI', 'coaxial', 'marker']
    far_rooms = [eh4l, wels, aclab, parcelb]

    Cable(random.choice(cable_types), random.choice(far_rooms))


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
    'down' : Direction('down'),
    'ask' : Ask(),
    'email' : Email(),
    'directory' : Directory()
}

def dispVerbs():
    print("Available Commands:")
    for verb in sorted(VERBS):
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

def intro():
    print ('Riccardo is a computing professor at Olin College. He leads a tough life.  The two are related.')
    enter()
    print('It\'s 9:00 AM.  Riccardo has not had his morning coffee.  However, he has prepared perhaps the best slideshow of his career.  It is his masterpiece, his magnum opus.  His David. His Mona Lisa.')
    print('To go with it, he has prepared a lecture that both Faulker and Hemingway would agree to envy.')
    enter()
    print('He gets to the classroom and fires up The Mainframe, his trusty computer. Though it has seen years of strife, it\'s scarred screen whirrs into life.')
    print('As eager students filter in, Riccardo pulls up Powerpoint, a silent tear appearing to commemorate its beauty. And then...')
    enter()
    print('The HDMI? The DVI? The VGA? SOMETHING! ANYTHING WILL DO. Give me a marker and I\'ll draw it if I have to!!!')
    print('Riccardo frantically searches to no avail. Alas, without a cable, the presentation cannot begin. The students gaze down anxiously as Riccardo begins to sob. Many edge out the door.')
    enter()
    print('One student remains behind. Gregleston steps forward and says, "Riccardo! It\'s alright. I saw a cable just the other day. I don\'t know where it is now, but it can\'t have gotten far! You can save the class, I BELIEVE IN YOU!"')
    enter()
    print('Riccardo\'s sobbing ceases. He dries his eyes with a brusque swipe of the sleeve. Standing boldly, he draws upon his years of teaching to lend him resolve. He quickly recalls the travails of the past, and how his superlative email and questioning abilities have steered him through similar trials. He knows the dangers. He knows the stakes. Thus begins the tale of...')
    enter()
    print(' _____  _                       _          ____                  _   ')
    print('|  __ \(_)                     | |        / __ \                | |      ')
    print('| |__) |_  ___ ___ __ _ _ __ __| | ___   | |  | |_   _  ___  ___| |_     ')
    print('|  _  /| |/ __/ __/ _` | \'__/ _` |/ _ \  | |  | | | | |/ _ \/ __| __|    ')
    print('| | \ \| | (_| (_| (_| | | | (_| | (_) | | |__| | |_| |  __/\__ \ |_     ')
    print('|_|  \_\_|\___\___\__,_|_|  \__,_|\___/   \___\_\\__,_|\___||___/\__|    ')


def enter():
    print('')
    input('Press \'Enter\' to continue...')
    print('')


def main():
    print('RiccardoQuest, version 1 (Fall 2014)\n')
    intro()
    # Create the world
    create_world()
    Player.clock.register(print_tick_action, 0)
    Player.me.look_around()


    while True:
        response = read_player_input ()
        print
        if response[0] == 'help': dispVerbs()
        elif response[0] in VERBS:
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                print("\n\n")
                Player.clock.tick()
                Player.me.look_around()
        else:
            print('What?')


if __name__ == '__main__':
    main()
