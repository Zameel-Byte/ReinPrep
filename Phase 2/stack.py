class Stack:
    arr = []
    size = 5

    def stack_push(self, element):
        if len(self.arr) >= self.size:
            return "Underflow: Queue Full"
        else:
            self.arr.append(element)

    def stack_pop(self):
        if len(self.arr) == 0:
            return "Underflow: Queue Empty"
        else:
            return self.arr.pop()

    def stack_peek(self):
        if len(self.arr) == 0:
            return "Underflow: Queue Empty"
        else:
            return self.arr[-1]

    def is_empty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False


obj1 = Stack()
obj2 = Stack()
for i in range(obj1.size):
    obj1.stack_push(i)
print(obj1.arr)

for j in obj1.arr:
    obj2.stack_push(obj1.stack_pop())
print(obj2.arr)
