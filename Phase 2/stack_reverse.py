from stack import Stack

obj1 = Stack()
obj2 = Stack()
for i in range(obj1.size):
    obj1.stack_push(i)
print(obj1.arr)

for j in range(len(obj1.arr)):
    obj2.stack_push(obj1.stack_pop())
print(obj2.arr)
