
class WObject (object):
    def __init__ (self,n):
        self.set_name(n)

    def name (self):
        return self._name

    def set_name(self, n):
        self._name = n.replace(' ', '-')

    def is_thing (self):
        return False

    def is_mobile_thing (self):
        return False

    def is_person (self):
        return False

    def is_room (self):
        return False

    def is_homework (self):
        return False

    def is_cable(self):
        return False

    def is_computer(self):
        return False

    def is_riccardo_computer(self):
        return False