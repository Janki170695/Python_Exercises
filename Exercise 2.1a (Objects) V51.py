#!/usr/bin/env python
# coding: utf-8

# <div style="background-color:black;">
# <img src="https://static.wixstatic.com/media/e99c3b_bf7763d953434005b731c2137dcad343~mv2.png/v1/fill/w_444,h_80,al_c,q_85,usm_0.66_1.00_0.01/TRADECRAFT-logo65-White.webp" width="300">
# </div>

# In[ ]:


## Object Types
An object's type determines the operations that the object supports (e.g., "does it have a length?") and also defines the possible values for objects of that type. Every object in Python has a type. Its type can be discovered by calling the *type()* built-in function. 

Show the object type for each of the following:
-  5
-  3.27
-  "True"
-  True


# In[1]:


type(5)   # Replace the dash with a value.


# In[2]:


type(3.27)


# In[3]:


type("True")


# In[6]:


type(True)


# What is the result of this command?  Explain why (in a comment in the code below)

# In[5]:


int(5.7)


# In[ ]:


##The function "int" converts the float value 5.7 to 5 .


# Change the integer **5** into a string and then show its type:

# In[7]:


type(str(5))  # Replace the dashes with the required function names.


# Try running this operation. 
# What is the result and why? (explain in a comment in the code below)

# In[8]:


5 + "5"


# In[ ]:


##The above statement throws an error because the datatype of both the arguments are different.
##Addition or concatenation cannot be performed between a string and an integer.


# Modify the two versions below so they will work. Explain the different result (in a comment in the code below)

# In[9]:


str(5) + "5"


# In[ ]:


##Here concatenation is performed between two arguments after converting "integer" value to "string".


# In[10]:


5 + int("5")


# In[ ]:


##Here addition is performed between two arguments after converting "string" value to "integer".


# -----------------
# <h2>Arithmetic</h2>
# 
# <p>Like every programming language, Python is a good calculator. Print out one calculation for each of these basic operations:</p>     
# 
# <ul>
#     <li>Addition</li>
#     <li>Subtraction</li>
#     <li>Multiplication</li>
#     <li>Division</li>
#     <li>Exponents</li>
# </ul> 

# In[11]:


print(10+10)


# In[12]:


print(10000-1000)


# In[13]:


print(456*789)


# In[27]:


print(28//7)


# In[18]:


print(2**3)


# * Calculate **0.1 + 0.2**   Is this the answer you would expect? 

# In[19]:


0.1+0.2


# In[ ]:


##Generally, everyone would assume the output to be 0.3, but it does not work that way with python interpreter.
##In binary with base-2, we can cleanly express the fractions that has denominator as 2, while rest would be repeating decimals.
##When we perform math over such fractions, it will have leftovers when we try to convert base-2 to base-10 representation.


# * Calculate **round(0.1 + 0.2, 1)**   What does the *round()* function do? 

# In[22]:


round(0.1+.2,1)


# In[ ]:


##The function round() is used to round the numbers by desired precision. Here, it rounds off to one digit precision.


# ## Order of Operations
# 
# Perform these calculations and explain the results in each case in a comment following the code.

# In[23]:


3 + 7 // 2


# In[ ]:


##Precedance of Division // is higher than addition +.(Also // performs the floor division)


# In[24]:


(3 + 7) // 2


# In[ ]:


##Precedence of () is higher than //


# In[25]:


3 + 7 % 2


# In[ ]:


## Precedence of Modulus % is greater than addition +. 


# In[26]:


(3 + 7) % 2


# In[ ]:


## Precedence of () is higher than %.

