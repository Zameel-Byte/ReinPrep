#!/usr/bin/env python
# coding: utf-8

# In[1]:


""" repetition operator
l=[1]*5
output: [1,1,1,1,1]
XOR Operaror
(^)"""
5^10
#day4
#OOP object oriented programming


# In[ ]:





# In[3]:


l=[1]*5
l


# In[ ]:


#packages
#from [filename] import [functionname]
#other way
#import [filename]  "file is an object.we are accessing using objects"
""" STUDENT IS A CLASS,name,roll no,etc are variables
actions:checking marks,attendance,etc(methods)"""
class Student:   #classname should start with capital letter-- naming conventions
    name=""          #class variables
    roll_num=""
    branch=""
    marks=0
    attendance=0.0
    is_using_bus=False
    def view_attendance(self) :       #class methods
        pass 
    def view_marks(self):        # self is a keyword which defines that particular method is belongs to certain class
        pass
    def view_name(self):
        pass
    def update_name(self,new_name):
        pass


# In[2]:


#CONSTRUCTOR DESTRUCTOR
""" constructor is also a method ,constructor is __init__
class S:
   def __init__(self):
       pass
we use constructors to default values to functions
#argumented constructor def __init__(self,name):
#what is a constructor and why do we use it?
"""
class Student:
    stu_name="no name"
    def __init__(self,name):
        print("Object created")
        print(name)
        print(self.stu_name)
        print(stu_name)
s1=Student("Aisshwarya")        


# In[3]:


class Student:
    stu_name="no name"
    def __init__(self,name):
        self.stu_name=name
s1=Student("Mukesh")  
s2=Student("rajesh")
s3=Student("karmesh")
print(s2.stu_name)


# In[8]:


class Student:
    stu_name="no name"
    def __init__(self,name):
        self.stu_name=name
    def update_name(self,new_name):
        self.stu_name=new_name
s1=Student("Mukesh")  
s2=Student("rajesh")
s3=Student("karmesh")
print(s2.stu_name)
s2.update_name("Aisshwarya")
print(s2.stu_name)


# In[12]:


class bank:
    def __init__(self,cus_name,cus_id,cus_branch):
        self.cus_name=cus_name
        self.cus_id=cus_id
        self.cus_branch=cus_branch
c1=bank("a",1,"smp")
c2=bank("b",2,"amp")
print(c1.cus_name,c1.cus_id,c1.cus_branch)
        


# In[14]:


class bank:
    def __init__(self,cus_name,cus_id,cus_branch):
        self.cus_name=cus_name
        self.cus_id=cus_id
        self.cus_branch=cus_branch
        print(self.cus_name,self.cus_id,self.cus_branch)
    
c1=bank("a",1,"smp")
c2=bank("b",2,"amp")


# In[ ]:


#enter name of custmer and print details of him/her


# In[ ]:


user2.print_details()
#encapsulation and abstraction
""" private variable ==    __[variable_name]
private variable are not accessible outside the class"""
#getter,setter methods


# In[7]:


#user part
class Userclass:
    full_name=""
    email=""
    __password="" #private variable
    mob_num=""
    def __init__(self,name,email,password):
        self.full_name=name
        self.email=email
        self.__password=password
        
    def update_name(self,new_name):
        self.full_name=new_name
    def get_name(self):  
        return self.full_name
    def change_password(self,new_password):  #setter method for private variable password
        self.__password=new_password
    def update_mobile_number(self,new_mobile_number):
        self.mobile_number=new_mobile_number
    def get_user_password(self):           #getter method for private variable password
        return self.__password
    
    
    


# In[8]:


#login part
#from User import Userclass #the above class
class Login:
    __db=[]
    def __init__(self):
        self.print_menu()
    def print_menu(self):
        print("welcome user")
        print("1.Register")
        print("2.login")
        print("3.exit")
    def create_user(self,user,name,email,password):
        new_user=Userclass(name,email,password)
        self.__db.append(new_user)
        return True
    def validate_user(self,email,password):
        temp=self.__db.copy()
        for user_obj in temp:
            if email==user_obj.email:
                if password==user_obj.get_user_password():
                    return "login sucessfully"
                else:
                    return "you entered wrong password"
        return "you are not registered with this email" #return false because email not found        
obj=Login()
while True:
    option=input("enter your choice:")
    if option=='1':
        name=input("Enter your full name:")
        email=input("Enter your email:")
        password=input("Enter your password:")
        res=obj.create_user(name,email,password)
        if res==True:
            print("user created successfully")
    elif option=='2':
        email=input("enter email")
        password=input("enter password")
        result=obj.validate_user(email,password)
        print(result)
        """if obj.validate_user(email,password):
            print("login successfully")
        else:
            print("login failed")"""
            
    elif option=='3':
        break
    else:
        print("Invalid Input")
    
        
        


# In[30]:


#validating email
email=input("Enter Email:")
if email[len(email)-10:]=="@gmail.com" and email[0].isdigit()==False and email[0].isalpha()==True:
    print("Valid email")
else:
    print("Invalid email")


# In[ ]:


email=input()
valid_char=['@','.']
if '@gmail.com'== email[-10]


# In[ ]:





# In[ ]:




