#!/usr/bin/env python
# coding: utf-8

# In[71]:


#Add item 70 and 60 after in the following python list
l1 =[10, 20, [30, 40, [50, 60], 80], 90, 100]
#output
##[10, 20, [30, 40, [50, 60, 70], 80], 90, 100]


# In[54]:


l2 = 70


# In[75]:


l1[2][2].append(l2)


# In[60]:


print (l1)


# In[61]:


#add sub list [7, 8]
l3 = [1,2,[3,4,5,6],9]
l4 = [7,8]


# In[70]:


l3[2].append([7,8])
print (l3)


# In[ ]:




