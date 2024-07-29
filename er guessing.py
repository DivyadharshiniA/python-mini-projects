#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
min=0
max=100
inputc=random.randint(min,max)
attempts=0
guess=False
print(f"Guess the number between {min} and {max}:")
while not guess:
    try:
        guessed=int(input())
        attempts+=1
        if guessed < min or guessed > max:
            print(f"Please enter a valid number between {min} and {max}")
        else:
            if guessed < inputc:
                print("You are less")
            elif guessed > inputc:
                print("You are larger")
            else:
                print(f"Congratulations! You've guessed the number {inputc} in {attempts} attempts.")
                guess = True
    except ValueError:
        print("Enter a valid number.")


# In[ ]:





# In[ ]:




