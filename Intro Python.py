
# coding: utf-8

# Introduction to python basics,this chapter includes understanding to keywords, operators.
# 

# **Basic Calculator:

# Python can be used as calculator

# In[2]:


a=1
b=2
a+b


# In[3]:


a/b


# In[5]:


a%b


# In[6]:


a-b


# In[7]:


b**2


# In[8]:


10+20


# In[9]:


print(a)


# In[10]:


a,b=10,100


# In[11]:


a


# __Enterkey and semicolon works as terminator.Here the 'a', 'b' are known as identifiers.
# Here are some rules to use identifires:
# 1.They must contain alpha numeric only.Special cases, black spaces are not allowed except('_') undersocre is allowed.
# 2.first letter can never be numeric,
# Check these some eg how identifires are not allowed (10a=1,a.1=1,a_?aa=20)

# #List of Keywords:

# [True, False, None, and , as , assert, break, class, continue, def, del, elif, if , else, except, for, finally, global, if,import , in, is , lambda, nonlocal, not, or, pass, raise, return,try, while, with, yield, async,await.....and many more]
# 
# 

# The usage of brackets:
# 
#     1.Paranthesis (): also known as tuple. It can contain list, dictionaries. Used for expression, functional agrument.
#     2.{}Curly brackets: To create a dictionary
#     3.[] Square brackets: To create list. Used for indexing and slicing.
# Hastag # used to comment. Anything after this will not be considered as code.

# In[25]:


lista=[1,2,3,4,5,7,9,22,66,a,b]


# In[26]:


tuplea=((1,a),lista)


# # Operators

# 1.Arithematic: +,-,*,/,//,**,%
# 
# 2.Rational: <,>,<=,>=,==,!=
# 
# 3.Assisment:=,+=,-=,*=,/=,//=,**=,%=
# 
# 4.Bitwise: &,|,^,>>,<<,~
# 
# 5.Logical: and, or, not
# 
# 6.Membership: in , not in
# 
# 7.Identity:is, is not
#     

# // :floor division, **: power, %:remainder, != :not equal to
# Assisment--> to write a=a+3
#             we can write a+=3.
**Few examples to use keywords and operators
# In[28]:


i=0
while i<10:
     print('hi')
     i+=1
     if i==4:
         break
     print('Bye')
print('Gone')


# In[31]:


i=0
while i<10:
     print('hi')
     i+=1
     if i==4:
         continue
     print('bye')
print('gone')


# In[34]:


i=0
while i<10:
     print('hi')
     if i==4:
         continue
     i+=1
     print('bye')
print('gone')
while not input():
     pass


# comprehension  there are three types
# 1.list
# 2.dictionary
# 3.generator

# In[36]:


a=[16,13,11,9,1,8,17,6]
b=[]
for i in a:
    b.append(i//2)


# In[37]:


b


# In[41]:


#dictionary comprehension
a=[16,13,11,9,1,8,17,6]
c={i:i*i for i in a}
a=[16,13,11,9,1,8,17,6]
d=[i for i in a if i%2==0]# here the ==0 will tell
a=[16,13,11,9,1,8,17,6]
e=[i*2 for i in a if i%2==0 and i<10]


# In[43]:


print(c)
print(d)
print(e)


# In[45]:


s='abcaddabc'
d={i:[s.count(i)] for i in s}

s1='hello you are you and hello are you'
w=s1.split()
d1={i:[w.count(i)]for i in w}


# In[46]:


d


# In[47]:


d1

