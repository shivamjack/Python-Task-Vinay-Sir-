#!/usr/bin/env python
# coding: utf-8

# In[3]:


###(.remove())


# In[5]:


# Example 1 (lst)
list1 = [ 1, 2, 1, 1, 4, 5 ]  
list1.remove(4)  
print(list1)   


# In[10]:


# Example 2 (str)
list2 = [ 'a', 'b', 'c', 'd' ]  
list2.remove('a')  
print(list2)


# In[7]:


# .count()
#Example 1 (lst)
list1 = [1, 1, 1, 2, 3, 2, 1] 
print(list1.count(1))  


# In[11]:


# Example 2 (str)
list2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b']   
print(list2.count('b'))


# In[24]:


# .clear
#Remove all elements from the list
#Example 1 
list1 = ["sova", "pheonix", "sage", "ryena"]


# In[28]:


list1.clear()
print (list1)


# In[29]:


#Example 2
list2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b']


# In[31]:


list2.clear()
print (list2)


# In[33]:


#.sort() #Arrange in ascending order
# Example 1
J = [1, 3, 4, 2] 
J.sort()
print(J) 


# In[34]:


#Example 2
M = [3, 3, 33, 443, 11, 49, 45, 43, 41]


# In[39]:


M.sort()
print (M)


# In[41]:


#.reverse()
#Example 1
list1 = ["sova", "pheonix", "sage", "ryena"]
list1.reverse()
print (list1)


# In[43]:


#Example 2
list2 = [ 'a', 'b', 'c', 'd' ]
list2.reverse()
print (list2)


# In[ ]:




