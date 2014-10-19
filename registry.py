import bisect
from types import MethodType


class Registry:

    def __init__(self):
        self._reg_list = []
        self._reg_dict = {}

    def add(self, task, priority):
        # Check if priority is already in the registry
        i = bisect.bisect_left(self._reg_list, priority)
        if i != len(self._reg_list) and self._reg_list[i] == priority:
            # And add only to the dict if so
            self._reg_dict[priority].append(task)

        # Otherwise add it to the list and dict
        else:
            self._reg_list.insert(i, priority)
            self._reg_dict[priority] = [task]

    def update(self, *args):
        for key in self._reg_list:
            for item in self._reg_dict[key]:
                if not self.remove(key, item):
                    item(*args)

    def remove(self, key, item):
        # Finds out if the owner of a method exists
        if isinstance(item, MethodType) and not item.__self__.location():

            # And, if not, deletes the method from the registry
            self._reg_dict[key].remove(item)
            if not self._reg_dict[key]:
                del self._reg_dict[key]
                bisect.bisect(self._reg_list, key)

            return True

    def __str__(self):
        list_str = ', '.join(str(i) for i in self._reg_list)
        dict_str = ', '.join("{}: {}".format(key, self._reg_dict[key]) for key in self._reg_list)
        return "{}\n{}".format(list_str, dict_str)
