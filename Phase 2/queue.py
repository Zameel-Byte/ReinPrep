class Queue:
    data = []
    size = 5

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


obj1 = Queue()
obj2 = Queue()
for i in range(obj1.size):
    obj1.enqueue(i)
print(obj1.data)

for j in obj1.data:
    obj2.enqueue(obj1.dequeue())
print(obj2.data)
