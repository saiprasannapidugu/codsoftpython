#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Password Generator

import random
import string
print("=== Password Generator ===")
length=int(input("Enter the desired password length: "))

# Create character pool
characters=string.ascii_letters+string.digits+string.punctuation

# Generate password
password=''.join(random.choice(characters)for _ in range(length))
print("Your Generated Password is:", password)


# In[ ]:




