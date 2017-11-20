class Stack: #Stack //first in last out

    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def push(self, e):
        self.stack.append(e)
        self.len_stack += 1

    def pop(self):
        if not self.empty():
            self.stack.pop(self.len_stack - 1)
            self.len_stack -= 1

    def top(self):
        return self.stack[-1]

    def empty(self):
        if self.len_stack == 0:
            return True
        return False

s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.top())
print(s.empty())
s.pop()
print(s.top())