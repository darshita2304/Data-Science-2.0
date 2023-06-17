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


# In[16]:


3+2+6+10


# In[17]:


21/4


# In[11]:


data.T


# In[19]:


meanbycol=np.mean(data,axis=0)


# In[15]:


np.mean(data.T,axis=1)


# In[21]:


data


# In[22]:


print(3-5.25)


# In[24]:


scaled_data=data-meanbycol


# In[26]:


scaled_data


# In[ ]:


#step-2 cov matrix becaue we want relation between variable


# In[29]:


cov_mat=np.cov(scaled_data.T)


# In[31]:


#step-3 eign value and eign vector
eig_val,eig_vec=np.linalg.eig(cov_mat)


# In[32]:


eig_val


# In[33]:


eig_vec


# In[ ]:


2*2


# In[35]:


scaled_data


# In[38]:


eig_vec.T.dot(scaled_data.T).T


# In[39]:


from sklearn.decomposition import PCA
pca=PCA()


# In[40]:


pca.fit_transform(scaled_data)


# In[41]:


pd.DataFrame(data=pca.fit_transform(scaled_data),columns=["PC1","PC2"])


# In[42]:


pca.inverse_transform(pca.fit_transform(scaled_data))


# In[44]:


scaled_data


# In[45]:


pca.explained_variance_ratio_


# In[46]:


0.90428109+0.09571891


# '''model for mcahine learning
# 
# there is two col
# 
# i ahve to choose one col
# 
# pc1 or pc2
# 
# pc1=representing more variation'''

# In[50]:


new_data=pd.read_csv("glass.data")


# In[52]:


new_data.head()


# In[67]:


#pd.read_csv("https://gist.githubusercontent.com/yifancui/e1d5ce0ba59ba0c275c0e2efed542a37/raw/dde7dbca24429542ff78964b83aaf064142dd771/data.csv").head()


# In[59]:


new_df=new_data.drop(labels=['index','Class'],axis=1)


# In[60]:


new_df.head()


# In[61]:


new_df.isnull().sum()


# In[63]:


new_df.describe().T


# In[64]:


#PCA
#step-1 standarization of the data
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()


# In[66]:


scale_data=scaler.fit_transform(new_df)


# In[70]:


scaled_df=pd.DataFrame(data=scale_data,columns=new_df.columns)


# In[71]:


scaled_df.head()


# In[73]:


scaled_df.describe().T


# ### eigen value and eigen vector is calculated internally in PCA library.
# 

# In[74]:


from sklearn.decomposition import PCA
pca=PCA()


# In[75]:


pca.fit_transform(scaled_df)


# In[77]:


scaled_df.shape


# In[78]:


pc_df=pd.DataFrame(data=pca.fit_transform(scaled_df))


# In[79]:


pc_df.shape


# In[80]:


pc_df.head()


# In[82]:


var=pca.explained_variance_ratio_


# In[88]:


var


# In[84]:


type(var)


# In[87]:


max(var)*100


# In[89]:


min(var)*100


# In[90]:


sum(var)


# In[ ]:


data=1
pca=all component(0.9999999999999998)


# In[91]:


1-0.9999999999999998


# In[96]:


var


# In[ ]:


np.sort(arr)[::-1]


# In[102]:


sum(sorted (var,reverse= True)[:6])


# In[92]:


plt.figure()
plt.plot(np.cumsum(var))
plt.xlabel("number of component")
plt.ylabel("variance")
plt.title("pca_repersentation")
plt.show()


# In[94]:


new_df.head()


# In[95]:


pc_df.head()


# In[103]:


PCA(n_components=6)


# ### when and when not we should use PCA?
# 

# In[ ]:




