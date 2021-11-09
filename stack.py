import queue

class Stack(object):
    def __init__(self):
        self.Stack = []

    def isEmpty(self):
        return len(self.Stack) == 0

    def push(self, data):
        self.Stack.append(data)

    def pop(self):
        max = len(self.Stack) - 1
        item = self.Stack[max]
        del self.Stack[max]
        return item