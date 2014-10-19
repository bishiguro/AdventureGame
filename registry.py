import bisect


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

    def update(self):
        for key in self._reg_list:
            for item in self._reg_dict[key]:
                item()

    def __str__(self):
        return ', '.join("{}: {}".format(key, self._reg_dict[key]) for key in self._reg_list)
