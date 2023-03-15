AY1
#DATATYPES
a="string"
print(type(a))
b=1
print(type(b))
c=10j
print(type(c))
l=[1,2]
print(type(l))
t=(1,2)
print(type(t))
s={1,2,3,1,2,3}
print(s,type(s))
#operators
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a and b)
print(a or b)
print(a & b)
print(a | b)
lst=[1,2,3,4,5,6]
print(1 in lst)
print(1 not in lst)
z=1
y=2
print(z is y)
print(z is not y)
# list medhds
lst.append(7)
print(lst)
lst.pop()
print(lst)
lst.pop(3)
print(lst)
lst.remove(1)
print(lst)
lst.extend([100,200,300])
print(lst)
lst.insert(0,500)
print(lst)
a=lst.count(2)
print(a)
b=lst.copy()
print(b)
b.clear()
print(b)
print(lst)
lst.sort()
print(lst)