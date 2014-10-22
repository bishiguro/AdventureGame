import sys
from player import *
from student import Student

SAME_ROUND = 1
NEXT_ROUND = 2  

class Verb (object):

    def act (self,input):
        if len(input)==0:
            return self.action0()
        if len(input)==1:
            wo1 = Player.me.thing_named(input[0])
            if wo1 is None:
                print('Word',input[0],'not understood')
                return SAME_ROUND
            return self.action1(wo1)
        if len(input)>1:
            wo1 = Player.me.thing_named(input[0])
            if wo1 is None:
                print('Word',input[0],'not understood')
                return SAME_ROUND
            wo2 = Player.me.thing_named(input[1])
            if wo2 is None:
                print('Word',input[1],'not understood')
                return SAME_ROUND
            return self.action2(wo1,wo2)

    def action0 (self):
        print('Input not understood')
        return SAME_ROUND

    def action1 (self,wo1):
        print('Input not understood')
        return SAME_ROUND

    def action2 (self,wo1,wo2):
        print('Input not understood')
        return SAME_ROUND



class Quit (Verb):

    def action0 (self):
        print('Goodbye')
        sys.exit(0)


class Direction (Verb):
    def __init__ (self,dir):
        self._direction = dir

    def action0 (self):
        if Player.me.go(self._direction):
            return NEXT_ROUND
        else:
            return SAME_ROUND


class Look (Verb):

    def action0(self):
        if not Player.god_mode:
            Player.me.look_around()
        else:
            for room in Room.getRooms():
                for item in room.contents():
                    actor.say('{} is in {}'.format(item.name(), room.name()))
            return SAME_ROUND

    def action1(self, obj1):
        obj1.look()
        return SAME_ROUND


class Wait (Verb):

    def action0 (self):
        return NEXT_ROUND

class Inventory(Verb):

    def action0(self):
        inv = Player.me.contents()
        if inv:
            Player.me.say(', '.join(thing.name() for thing in inv))
        else:
            Player.me.say("Inventory empty.")
        return SAME_ROUND

class God (Verb):

    def action0 (self):
        if Player.god_mode:
            Player.god_mode = False
        else:
            Player.god_mode = True
        print('(God mode is now','on)' if Player.god_mode else 'off)')
        return SAME_ROUND


class Use (Verb):

    def action1 (self,obj):
        obj.use(Player.me)
        return SAME_ROUND


class Take (Verb):

    def action1 (self,obj):
        if not obj in Player.me.contents():
            obj.take(Player.me)
        else:
            Player.me.say("I already have {}".format(obj.name()))

        return SAME_ROUND

class Drop (Verb):

    def action1 (self,obj):
        if not Player.me.have_thing(obj):
            Player.me.say('I am not carrying '+obj.name())
        else:
            obj.drop(Player.me)
        return SAME_ROUND

class Give (Verb):

    def action2 (self,obj1,obj2):
        if isinstance(obj2, Person):
            obj1.give(Player.me,obj2)
        else:
            Player.me.say("I can't give an object to {}.".format(obj2.name()))
        return SAME_ROUND


class Ask (Verb):

    def action1(self, obj1):
        if isinstance(obj1, Student):
            obj1.ask()
        else:
            Player.me.report("I don't think that {} knows anything ".format(obj1) +
                             "about the cable. You should try asking a student.")


class Email (Verb):

    def act(self, target):
        if len(target) == 1:
            name = target[0]

            # Catch invalid entries
            if not name == 'all-students' and not name in Student._all_students:
                Player.me.say("I don't think that {} is a student here.".format(name))
            else:
                return self.action1(name)

        # Catch invalid arguments
        else:
            print("Who did you want to email? Try their name, or 'all-students'.")

        return SAME_ROUND

    def action1(self, name):
        if name in Student._all_students:
            self.read_email(Student.email_student(name))
        else:
            emails_back = Student.email_all_students()
            for email in emails_back:
                if email:
                    self.read_email(email)

        return NEXT_ROUND

    def read_email(self, email):
        if email:
            Player.me.report("{} writes:\n{}".format(*email))
        else:
            Player.me.report("You wait for some time for a response, but receive nothing.")


class Directory (Verb):

    def action0(self):
        Player.me.report("STUDENTS of OLIN COLLEGE:")
        for s in Student._all_students:
            Player.me.report(" --{}".format(s))
        return SAME_ROUND
