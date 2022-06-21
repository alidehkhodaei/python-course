class Counter:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            num = self.start
            self.start += self.step
            return num
        raise StopIteration


for i in Counter(10, 20):
    print(i)
