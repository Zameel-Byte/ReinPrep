class Queue:
    def __init__(self):
        self.data = []
        self.size = 5

    def enqueue(self, element):
        if len(self.data) >= self.size:
            return "Underflow: Queue Full"
        else:
            self.data.append(element)

    def dequeue(self):
        if len(self.data) == 0:
            return "Underflow: Queue Empty"
        else:
            return self.data.pop(0)

    def queue_peek(self):
        if len(self.data) == 0:
            return "Underflow: Queue Empty"
        else:
            return self.data[-1]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def queue_print(self):
        print(self.data)
