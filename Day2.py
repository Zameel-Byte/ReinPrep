
#tuple methods
tup=(0,2,3,4,5,6,7,1,2,3)
a=tup.index(1)
print(a)
b=tup.count(2)
print(b)


#set methods
s1={1,2,3,4}
s2={3,4,5,6}
res1=s1.intersection(s2)   
res2=s1.union(s2)           
res3=s1.difference(s2)      
res4=s2.difference(s1)      
print(res1)
print(res2)
print(res3)
print(res4)






# program to determine whether the given input is even or odd number
n=int(input()) # n is the number to be determined whether it is even or odd
if n%2==0:     # any number divided by 2 is considered as even
    print(n,"is even")
else:
    print(n,"is odd")    
#program to determine weekdays
n=int(input())
if n<1 or n>7:
    print("You entered invalid number.PLease re enter the number to proceed")
elif n==1:
    print("Sunday")
elif n==2:
    print("Monday")
elif n==3:
    print("Tuesday")
elif n==4:
    print("Wednesday")
elif n==5:
    print("Thusday")
elif n==6:
    print("Friday") 
else:
    print("Saturday")                       
#weird num n is 0> to <20  even == weird if not normal  ,n>=20 noraml number ,n>=30 and odd === noraml number 
n=int(input())
if n>0 and n<20:
    if n%2==0:
        print("WEIRD NUMBER")
    else:
        print("NORMAL NUMBER")
elif n>=20 and n<30:
    print("NORMAL NUMBER")
else:
     if n%2==0:
         print("WEIRD NUMBER")
     else:
         print("NORMAL NUMBER")


#to find index of element with value          
l=[1,2,3,4,56,78,0]
a=int(input())
flag=False
for i in range(len(l)):
    if l[i]==a:
        flag=True
        break
if flag==True:
    print("Element found at index ",i)
else:
    print("Element is not there in list")    
# finding the index of element in list with index method
l=[100,3,400,50,96]
a=l.index(400)
print(a)
# different methods in list
l=[]
for i in range(10):
    l.append(i)
print(l)     

l2=[i for i in range(0,10)]
print(l2)

l3=[i for i in range(0,51,2)]
print(l3) # l3=[i for i in range(0,51) if i%2==0]

# list contains numbers divisible by both 7 and 11 in the range 1 and 100
l4=[i for i in range(1,101) if i%7==0 and i%11==0]
print(l4)

#reversing a list without reverse function
l=[1,2,3,4,5,6]
l2=[]
for i in range(len(l)):
    l2.append(l[-1])
    l.pop()
print(l2)


#finding sum of all negative numbers and sum of positive numbers in a list and finally adding both of them 
po_sum=0
neg_sum=0
l=list(map(int,input().split()))
for i in l:
    if i<0:
        neg_sum=neg_sum+i
    elif i>0:
        po_sum=po_sum+i
    else:
        continue
print(po_sum+neg_sum)
print(sum(l))         

         