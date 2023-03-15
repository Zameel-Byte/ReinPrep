from queue import Queue
from stack import Stack

obj1 = Queue()
obj2 = Stack()
for i in range(obj1.size):
    obj1.enqueue(i)
print(obj1.data)

for j in range(len(obj1.data)):
    pop_ele = obj1.dequeue()
    obj2.stack_push(pop_ele)
print(obj2.arr)
