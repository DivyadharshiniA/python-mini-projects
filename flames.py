#!/usr/bin/env python
# coding: utf-8

# In[2]:


name1=input("Enter name1:").replace(" ","").lower()
name2=input("Enter name2:").replace(" ","").lower()
for char in name1[:]:
    if char in name2:
        name1=name1.replace(char,'',1)
        name2=name2.replace(char,'',1)
tot=len(name1)+len(name2)
flames=['F','L','A','M','E','S']
while len(flames)>1:
    split=(tot % len(flames))-1
    if split>0:
        right=flames[split+1:]
        left=flames[:split]
        flames=right+left
    else:
        flames=flames[:len(flames)-1]
flames_meaning = {
    'F': "Friends",
    'L': "Lovers",
    'A': "Affectionate",
    'M': "Married",
    'E': "Enemies",
    'S': "Siblings"
}
result=flames[0]
relationship=flames_meaning[result]
print("The relationship between two names is")
print(relationship)


# In[ ]:





# In[ ]:




