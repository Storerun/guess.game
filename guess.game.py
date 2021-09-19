#!/usr/bin/env python
# coding: utf-8

# In[8]:


# this game guesses the number of oranges in a box.( a game of chance)


# In[9]:


orange_num= 13
guess_count=0
guess_limit= 3


# In[11]:


while guess_count < guess_limit:
    guess=int(input("Guess number: "))
    guess_count=guess_count+1
    if guess == orange_num:
        print("YOU WON")
        break
else:
    print("SORRY, GAME OVER")
    


# In[ ]:




