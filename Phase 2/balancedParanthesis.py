from stack import Stack as Sk

s1 = Sk()

inp = "(())()"

for ele in inp:
    if ele == "(":
        s1.stack_push(ele)
    elif ele == ")" and len(s1.arr) != 0:
        s1.stack_pop()
    else:
        print("Wrong")
if len(s1.arr) == 0:
    print("Correct")
else:
    print("Wrong")
