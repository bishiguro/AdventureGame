
class WObject (object):
    def __init__ (self,n):
        self._name = n.replace(' ', '-')

    def name (self):
        return self._name
      
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
