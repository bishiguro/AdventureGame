from registry import Registry


class Clock (Registry):

    def __init__(self, time=0):
        self._time = time
        super(Clock, self).__init__()

    def register(self, f, priority):
        self.add(f, priority)

    def deregister(self, f):
        self.remove(f)

    def tick(self):
        self.update(self._time)
        self._time += 1
