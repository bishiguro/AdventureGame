import random
from room import *
from player import Player
from cable import Cable
from npc import NPC


class Student(NPC):
    _all_students = {}
    _first_ext = ["", "bat", "super", "mega", "best", "127", "283", "l33t", "xx", "#hashtag", "hashtag", "#"]
    _second_ext = ["prosnipes", "360noscope", "wizard", "nopants", "hashtag", "selfie"]
    _domains = ["aol.com", "gmail.com", "yahoo.com", "toteslegit.ru", "bestemail.co", "we'rehip.io"]
    _no_response = "You wait for some time, but recieve no response to your email."

    @staticmethod
    def email_student(student_name):
        return Student._all_students[student_name].email()

    @staticmethod
    def email_all_students():
        Player.me.report("Even as you hit the send button, " +
                         "you feel the combined wroth of the student body " +
                         "roll over you, so malevolently that it actually hurts.")
        Player.me.suffer(1)

        email_list = []
        for s in Student._all_students:
            response = Student._all_students[s].email()
            if response:
                email_list.append(response)

        return email_list

    def __init__(self, name, loc, desc="A student of Olin College."):
        super(Student, self).__init__(name, loc, desc)
        Student._all_students[name] = self
        self._techy = random.randint(1, 4)
        self._cable_info = None

        first_ext = random.choice(Student._first_ext)
        second_ext = random.choice(Student._second_ext)
        domain = random.choice(Student._domains)
        self._email = "{}{}{}@{}".format(name, first_ext, second_ext, domain)
        Player.me.clock.register(self.checkForCable, 4)

    def email(self):
        info = self.getInfo()
        if not info:
            return None

        response_body = "{}\n-{}".format(info, self.name())
        return self._email, response_body

    def ask(self):
        if isinstance(self._cable_info, Cable):
            self.say("Sure, I have it right here!")
            self._cable_info.give(self, Player.me)
            self.say("By the way, is there any chance I could get into FoCS next semester?")
            self.report("You gently shake your head and  softly murmer a 'no' both assertive and melancholy.")

        else:
            info = self.getInfo()
            if not info:
                self.report("{} stares at you vapidly for a second, then gets distracted by a passing whimsy. ".format(self.name()) +
                            "You suspect that {} is not aware of the whereabouts of the cable, and further induce ".format(self.name()) +
                            "that {} has not slept for a good long time.".format(self.name()))

            else:
                self.say(info)

    def getInfo(self):
        if not self._cable_info or isinstance(self._cable_info, Cable):
            return None

        owner = self._cable_info[0]
        place = self._cable_info[1]

        choices = ["I last saw it in {}.".format(place.name())]

        if owner:
            choices.extend(["I last saw {} with it.".format(owner.name()),
                    "I saw {} with it in {}".format(owner.name(), place.name())])

        return random.choice(choices)

    def enter_room(self):
        super(Student, self).enter_room()
        self.checkForCable()


    def cableNotify(self, cable):
        if not self.tryTakeCable(cable):
            self.recordInfo(cable)

    def checkForCable(self, *args):
        if not self.has_cable():
            everything = self.peek_around()
            for thing in everything:
                if isinstance(thing, Cable):
                    self.cableNotify(thing)

    def tryTakeCable(self, target):
        if random.randint(1, 5) <= self._techy:
            owner = target.location()
            self.say("Thanks, {}, this is just the cable I was looking for!".format(owner.name()))
            target.take(self)
            self.move_somewhere()
            return True

    def add_thing(self, thing):
        if isinstance(thing, Cable):
            self._cable_info = thing

        super(Student, self).add_thing(thing)

    def lose(self, t, loseto):
        if isinstance(t, Cable):
            self._cable_info = (loseto, self.location())

        super(Student, self).lose(t, loseto)

    def recordInfo(self, cable):
        owner = cable.location()
        if not isinstance(owner, Person):
            owner = None

        self._cable_info = (owner, self.location())

    def destroy(self):
        del Student._all_students[self.name()]
        super(Student, self).destroy()


if __name__ == "__main__":
    l = Room("TestRoom")
    p = Player("Riccardo", l)

    c = Cable("The vaunted cable", l)
    cypress = Student("Cypress", l)
    bonbon = Student("Bonskilaylay", l)

    c.move(cypress)
    bonbon.cableNotify(c)

    bonbon.ask()
    cypress.ask()
