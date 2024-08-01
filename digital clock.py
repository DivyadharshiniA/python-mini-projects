#!/usr/bin/env python
# coding: utf-8

# In[11]:


import tkinter as tk
import time

root = tk.Tk()
root.title("Digital clock")
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')
def updatetime():
    ct=time.strftime("%H:%M:%S")
    label.config(text=ct)
    label.after(1000,updatetime)
updatetime()
root.mainloop()


# In[ ]:





# In[ ]:




