#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install rotate-screen


# In[6]:


import rotatescreen
import time


# In[11]:


screen = rotatescreen.get_primary_display()
for i in range(13):
    time.sleep(1)
    screen.rotate_to(i*90 % 360)


# In[ ]:




