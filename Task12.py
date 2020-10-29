#!/usr/bin/env python
# coding: utf-8

# In[1]:


#reduce function
#ex1


# In[5]:
#first we have to import the function from functools

from functools import reduce


# In[9]:


a = [10,20,30,40,50,60,70,80,90]

Sum_of_a = reduce(lambda j,k:j+k, a)

print(Sum_of_a)


# In[10]:


#ex2


# In[20]:


B = range(1,11)
C = list(B)
print(B)


# In[21]:


multiply_of_all= reduce(lambda j,k:j*k ,C)
print(multiply_of_all)


# In[22]:


#zip function


# In[ ]:


#ex1


# In[23]:


a=["sage","ryena","killjoy"]
b=[70,150,12]
c= zip(a,b)


# In[24]:


print(c)


# In[25]:


d=list(c)
print(d)


# In[26]:


#ex2


# In[32]:


e=[1,2,3,4,5]
f=["jack","noob","eddy"]
g=list(zip(e,f))
print(g)


# In[33]:


#enumerate


# In[34]:


#ex1


# In[35]:


h=["sova","sage","omen","rage"]
enm=enumerate(h)


# In[36]:


print(enm)


# In[37]:


eml_lst=list(enm)
print(eml_lst)


# In[38]:


i=["jackknife","pheonix","cypher","jet"]
k=list(enumerate(i))
k


# In[ ]:




