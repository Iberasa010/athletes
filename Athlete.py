from sanitizer import sanitizer


class Athlete:

    def __init__(self, name, dob=None, times=None):
        self.name = name
        self.dob = dob
        self.times = times

    def top3(self):
        return sorted(set([sanitizer(t) for t in self.times]))[0:3]

    def add_time(self, time):
        if self.times is None:
            self.times = []
        self.times.append(time)

    def add_times(self, list_of_times):
        if self.times is None:
            self.times = []
        self.times.extend(list_of_times)


'''
ema = Athlete("Ema")
ema.add_time('2:33')
print(ema.times)
ema.add_times(['1:57', '2:15'])
print(ema.times)
'''