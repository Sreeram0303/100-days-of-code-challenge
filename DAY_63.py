#Implementation of stack using queue


class Stack:
    def __init__(self):
        self.q = Queue()


    def push(self, x):
        s = self.q.qsize()
        self.q.put(x)
        for i in range(s):
            self.q.put(self.q.get())


    def pop(self):
        n = self.q.get()
        return n


    def top(self):
        return self.q.queue[0]


    def size(self):
        return self.q.qsize()