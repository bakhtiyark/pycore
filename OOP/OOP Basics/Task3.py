class Counter:
    def __init__(self, start=0, stop=None) -> None:
        self.start = start
        self.stop = stop
    def increment(self):
        if (self.stop == None):
            self.start = self.start + 1
        elif (self.start<self.stop):
            self.start = self.start + 1
        else:
            return "Maximum value is reached"
    def get(self):
        return self.start

count = Counter(0, 3)
count.increment()
print(count.get())
count.increment()
print(count.get())
count.increment()
print(count.get())
