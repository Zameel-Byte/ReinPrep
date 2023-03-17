class Stack:
    def __init__(self):
        self.arr = []
        self.size = 10

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

    def stack_print(self):
        print(self.arr)
