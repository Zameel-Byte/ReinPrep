#!/usr/bin/env python
# coding: utf-8

# In[1]:


#string methods
s="hello world"
s.capitalize()


# In[2]:


s.split(' ')


# In[3]:


s


# In[4]:


s.split()


# In[5]:


s.split('')


# In[6]:


p='hello@world'
p.split('@')


# In[8]:


l=['a','b']
''.join(l)


# In[9]:


' '.join(l)


# In[10]:


'and'.join(l)


# In[11]:


#when we split string the output produced is list 
#join is used to form string from list
s.title()


# In[13]:


s1="abcd"
s2="ABCD"
print(s1.upper())
print(s2.lower())


# In[14]:


'hello world'.count('l')


# In[15]:


s1.isdigit()


# In[17]:


s1.isalpha()


# In[19]:


s1.isalnum()


# In[20]:


s1.swapcase()


# In[21]:


d='abCD'
d.swapcase()


# In[22]:


f='12ab'
f.isalnum()


# In[23]:


g='ab'
g.isalnum()


# In[24]:


h="@abc"
h.isalnum()


# In[26]:


#string formating
first="I am "
age=20
last=" years old"
print(first+str(age)+last)
print("I am {} years old".format(age)) #string formatting


# In[28]:


print("I am {} years and {} months old".format(20,3))


# In[32]:


print("I am {} years and {:.100f} months old".format(20,3))


# In[35]:


print("I am {:10} years and {:10.2f} months old".format(20,3)) #spaces


# In[36]:


#fstrings
num=10
print(f"the square of {num} is {num*num:.5f}")


# In[38]:


#calculator using python
#Exception handling 
a=int(input())
b=int(input())
try:
    print(a/b)
except:
    print("b cannot be zero")
print("after the error")    


# In[43]:


a=int(input())
b=int(input())
operator=input()
l=['+','-','*','/','%']
if operator in l:
    if operator=='+':
        print(a+b)
    elif operator=='-':
        print(a-b)
    elif operator=='*':
        print(a*b) 
    elif operator=='%':
        try:
            print(a%b)
        except:
            print("Denominator cannot be zero")
    
    else:
        try:
            print(a/b)
        except:
            print("Denominator cannot be zero")
else:
    print("please enter valid operator")


# In[ ]:




