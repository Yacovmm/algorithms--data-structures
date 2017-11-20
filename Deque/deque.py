class Deque:

    def __init__(self):
        self.deque = []
        self.len = 0

    def empty(self):
        if self.len == 0:
            return True
        return False

    def push_front(self, e):
        self.deque.insert(0, e)
        self.len += 1

    def push_back(self, e):
        self.deque.insert(self.len, e)
        self.len += 1

    def pop_front(self):
        if not self.empty():
            self.deque.pop(0)
            self.len -=1

    def pop_back(self):
        if not self.empty():
            self.deque.pop(self.len - 1)
            self.len -=1

    def front(self):
        if not self.empty():
            return self.deque[0]

    def back(self):
        if not self.empty():
            return self.deque[-1]

    def show(self):
        for i in self.deque:
            print(i, end=' ')

d = Deque()
print(d.empty())
d.push_front(10)
d.push_front(5)
d.push_back(20)

print(d.empty())
d.show()

