#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time
import datetime
import winsound
i=input("Enter time in (HH:MM:SS) :")
ct=datetime.datetime.now().strftime("%H:%M:%S")
print("Current time is "+ct)
while True:
    ct=datetime.datetime.now().strftime("%H:%M:%S")
    if ct==i:
        print("It's time to wake!")
        winsound.Beep(1000,1000)
        break
    time.sleep(1)


# In[ ]:




