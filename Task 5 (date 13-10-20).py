#!/usr/bin/env python
# coding: utf-8

# In[21]:


dict1 = {"april_batch"
         :{"student":{"name":"Mike", "marks":{"python":80, "maths":70}}}}


# In[2]:


#access mike


# In[3]:


dict1["april_batch"]["student"]["name"]


# In[4]:


#access 80


# In[6]:


dict1["april_batch"]["student"]["marks"]["python"]


# In[7]:


#Change name mike to Jack


# In[22]:


dict1["april_batch"]["student"]["name"]="Shivam_jack"


# In[10]:


print(dict1)


# In[14]:


##Add ML =80 and DL =80 inside marks


# In[25]:


dict1["april_batch"]["student"]["marks"]["ML"] = 80
print(dict1)


# In[26]:


dict1["april_batch"]["student"]["marks"]["DL"] = 80
print(dict1)


# In[ ]:




