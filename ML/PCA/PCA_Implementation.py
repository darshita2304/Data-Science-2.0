#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import statement
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eig
from numpy.linalg import eig


# In[3]:


#two dimension data
data=np.array([[3,4],[2,8],[6,9],[10,12]])


# In[4]:


print(data)


# In[8]:


#create dataframe
df=pd.DataFrame(data,columns=["ML","DL"])


# In[9]:


df


# In[10]:


plt.scatter(df["ML"],df["DL"])


# In[ ]:


#PCA-Steps
1 standarization of the data(ZERO centric data)
2 cov matrix
3 eig value and eig vector
4 find Principle component


# In[12]:


data


# In[11]:


data.T


# In[ ]:




