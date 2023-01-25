#!/usr/bin/env python
# coding: utf-8

# In[1]:


#day 5
#inheritance
""" types of inheritance: single inheritance,multilevel inheritence,hierarchial inheritance,multiple inheritence
    multiple inheritance is only supported by python directly  """
class A:
    name="Aisshu"
    age=36
    pass
class B(A):   #B is inherting from A
    age=10
obj=B()
print(obj.age)
print(obj.name)


# In[2]:


class A:
    name="Aisshu"
    age=36
    pass
class B(A):   #B is inherting from A
    age=10
obj=B()
obj.name="Aisshwarya"
print(obj.age)
print(obj.name)


# In[3]:


class a:
    name="aisshu"
class b(a):
    age=10
class c(b):
    height=170
obj=c()
print(obj.name)
print(obj.age)
print(obj.height)


# In[5]:


#multilevel inheritance
class Grandpa:
    color="black"
    job="doctor"
class Father(Grandpa):
    color="white"
class Son(Father):
    age=12
obj=Son()
print(obj.color)
obj2=Father()
print(obj2.job)
print(obj.job)


# In[7]:


#hierarchial inheritance
class Animal:
    food="eats something"
class PetAnimal(Animal):
    living_place="home"
class WildAnimal(Animal):
    living_place="forest"
obj1=WildAnimal()
obj2=PetAnimal()
print(obj1.food)
print(obj2.food)
print(obj1.living_place)
print(obj2.living_place)


# In[ ]:


#another example of hierarchial inheritance
class Person:
    name=""
    gender=""
    age=""
class Student(Person):
    roll_num=""
    branch=""
class Faculty(Person):
    salary=""
    subject=""
    reportsTo=""
class VC(Person):
    def give_salary(self):
        pass
    def takes_fees(self):
        pass
    


# In[ ]:


#multiple inheritance
#diamond problem  in java solve by interfaces
#python interpreter is smart--> it takes first argument


# In[9]:


#example of multiple inheritance
class Father:
    color="white"
    def pos_trait(self):
        print("Quick Thinker")
class Mother:
    color="black"
    def pos_trait(self):
        print("soft hearted")
class Daughter(Father,Mother):
    pass
obj=Daughter()
print(obj.color)
obj.pos_trait()


# In[10]:


#hybrid inheritance
#one common example : hierarchial+multiple
class Vehicle:
    usage="to travel"
class Twowheeler(Vehicle):
    purpose="short distance"
class Fourwheeler(Vehicle):
    purpose="long distance"
class Person(Twowheeler,Fourwheeler):
    pass
obj=Person()
print(obj.usage)
print(obj.purpose)


# In[ ]:


#exit codes  / error codes
# exit code 0: successful execution
# exit code 1: 
# frameworks
#frontend is important for anything
#saps-- used to build portals --- Accenture         highly efficent
#digital marketing-- ads -----udemy


# In[ ]:


#rock paper scissors game
import random
print("Lets play")
print("CHOOSE:\n0 FOR ROCK\n1 FOR SCISSOR\n2 FOR PAPER")
user_choice=int(input())
L=["ROCK","PAPER","SCISSOR"]
print("USER CHOICE: ",L[user_choice])
computer_choice=random.randint(0,3)
print("COMPUTER CHOICE: ",L[computer_choice])
print(computer_choice)
if user_choice==computer_choice:
    print("BOTH WON")
elif (user_choice==0 and computer_choice==1) or(user_choice==1 and computer_choice==2) or (user_choice==2 and computer_choice==0):
    print("USER WON")
else:
    print("COMPUTER WON")


# In[ ]:


#rock paper scissors game
import random
print("Lets play")
print("CHOOSE:\n0 FOR ROCK\n1 FOR SCISSOR\n2 FOR PAPER")
user_choice=int(input())
L=["ROCK","PAPER","SCISSOR"]
print("USER CHOICE: ",L[user_choice])
computer_choice=random.randint(0,3)
print("COMPUTER CHOICE: ",L[computer_choice])
print(computer_choice)
if user_choice==computer_choice:
    print("BOTH WON")
elif (user_choice==0 and computer_choice==1) or(user_choice==1 and computer_choice==2) or (user_choice==2 and computer_choice==0):
    print("USER WON")
else:
    print("COMPUTER WON")


# In[ ]:


#rock paper scissors game with who won first by scoring n points first
import random
print("Lets play")
a=3
user_win=0
comp_win=0
for i in range(a):
    print("CHOOSE:\n0 FOR ROCK\n1 FOR SCISSOR\n2 FOR PAPER")
    user_choice=int(input())
    L=["ROCK","PAPER","SCISSOR"]
    print("USER CHOICE: ",L[user_choice])
    computer_choice=random.randint(0,2)
    print("COMPUTER CHOICE: ",L[computer_choice])
    if user_choice==computer_choice:
        user_win += 0
        comp_win += 0
    elif (user_choice==0 and computer_choice==1) or(user_choice==1 and computer_choice==2) or (user_choice==2 and computer_choice==0):

        user_win += 1
    else:
        comp_win += 1
    print("Present score of user:",user_win)
    print("Present score of computer:",comp_win)    
    if user_win==a or comp_win==a:
        if user_win==a:
            print("USER WINS")
        else:
            print("COMPUTER WINS")
    
    


# In[ ]:


#casino game


# In[1]:


#polymorphism
class A:
    def method_1(self,a,b):
        print("sum of 2 numbers",a+b)
class B(A):
    def method_1(self,a,b):
        print("prod of 2 numbers",a*b)
obj=B()
obj.method_1(10,20)           #METHOD IS OVERIDDEN  ---- METHOD OVERRIDING ---RUNTIME POLYMORPHISM


# In[5]:


class A:
    def method_1(self,a,b):
        print("sum of 2 numbers",a+b)
class B(A):
    def method_1(self,abc):
        print("value is",abc)
    def method_1(self,a,b):
        print("prod of 2 numbers",a*b)
obj=B()
obj.method_1(100)         #method overloading ------------COMPILETIME POLYMORPHISM


# In[6]:


class A:
    def method_1(self,a,b):
        print("sum of 2 numbers",a+b)
class B(A):
    def method_1(self,abc):
        print("value is",abc)
    def method_1(self,a,b):
        print("prod of 2 numbers",a*b)
obj=B()
obj.method_1(100,200)


# In[ ]:


#work: validating username and password in login systems

#rock paper scissors game
from random import randint
choice = ['rock', 'paper', 'scissor']
p_score = 0
c_score = 0
limit = 3
while p_score != limit and c_score != limit:
    print(f"choose among the following: ", choice)
    my_ch = input("Player choice: ").lower()
    if my_ch not in choice:
        print("Invalid input")
        continue
    sys_ch = choice[int(randint(0,2))]
    print(f"System choice: {sys_ch}")
    if my_ch == sys_ch:
        print("---DRAW---")
        continue
    if my_ch == "rock" and sys_ch == "scissor":
        p_score += 1
    elif my_ch == "paper" and sys_ch == "rock":
        p_score += 1
    elif my_ch == "scissor" and sys_ch == "pape
