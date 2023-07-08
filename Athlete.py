from sanitizer import sanitizer


class AthleteList(list):

    def __init__(self, name, dob=None, times=None):
        list.__init__([])
        if times is None:
            times = []
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return sorted(set([sanitizer(t) for t in self]))[0:3]

    def add_time(self, time):
        self.append(time)

    def add_times(self, list_of_times):
        self.extend(list_of_times)



