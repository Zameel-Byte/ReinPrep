from stack import Stack as Sk

s = Sk()
s2 = Sk()
for i in range(s.size):
    s.stack_push(i)
print(s.arr)
num = int(input())
count = 0
for j in range(len(s.arr)):
    pop_ele = s.stack_pop()
    if num == pop_ele:
        count = + 1
    else:
        pass
if count >= 1:
    print("element found")
else:
    print("not")
