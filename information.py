import random


class Information:

    def __init__(self, suspect):
        self._loc = suspect.loc.name()
        self._suspect = suspect.name()

    def __str__(self):
        return random.choice(["I last saw {} with it.".format(self._suspect),
                              "I last saw it in {}.".format(self._loc)])
