import NPC

"""
    - On enter:
        - Student has a random chance to take cable (1/5 - 4/5)
        - Student records info on where they last saw the cable

    - On ask:
        - Student replies I don't know if they don't know
        - Student replies I have it and gives it to you if they do
        - Student gives both pieces of information if they know something

    - On email:
        - Student sends one piece of info, both, or no response
        - Student email addresses includes students name, some random characters, and a domain

    - On email AllStudents
        - Invokes email on every student

    - Check if cable is taken in accept method and set information accordingly

"""

class Student(NPC):
    _all_students = {}
    _first_ext = ["", "bat", "super", "mega", "best", "127", "283", "l33t", "xx", "#hashtag", "hashtag", "#"]
    _second_ext = ["prosnipes", "360noscope", "wizard", "nopants", "hashtag", "selfie"]
    _domains = ["aol.com", "gmail.com", "yahoo.com", "toteslegit.ru", "bestemail.co", "we'rehip.io"]


    def emailAllStudents(self, sender):
        sender.location().report("Even as you hit the send button, " +
                                 "you feel the combined wroth of the student body " +
                                 "roll over you, so malevolently that it actually hurts.")
        sender.suffer(1)

        info_list = 
        for student in Student._all_students:
            email(student)

        return responses

    def __init__(self, name, loc):
        super(Student, self).__init__(name, loc)
        self._techy = random.randint(1, 4)
        self._cable_info = None

        first_ext = random.choice(Student._first_ext)
        second_ext = random.choice(Student._second_ext)
        domain = random.choice(Student._domains)
        self._email = "{}{}{}@{}".format(name, first_ext, second_ext, domain)

    def enter_room (self):
        if not self.has_cable():
            target = self.checkForCable():
            if target:
                self.cableNotify(target)

        super(Student, self).enter_room()

    def cableNotify(self, target):
        if not self.tryTakeCable():
            self.recordInfo(target)

    def checkForCable(self, target):
        everything = self.peek_around()
        for thing in everything:
            if isinstance(thing, Cable):
                return thing

    def tryTakeCable(self, target):
        if random.randint(1, 5) <= self._techy:
            target.take(self)
            self._cable_info = target
            return True

    def lose(self, t, loseto):
        if isinstance(t, Cable):
            self.recordInfo(loseto)

        super(Student, self).lose(t, loseto)

    def recordInfo(self, target):
        self._cable_info = (target, self.location())