#K-means
'''1.Unsupervised learning algorithm
2.The task is to classify the items into groups.
3.To calculate we use euclidean distance as measurement.
4.The algorithm works as follows:
    First we initialize k points, called means, randomly.
    We categorize each item to its closest mean and we update the mean’s coordinates, which are the averages of the items categorized in that mean so far.
    We repeat the process for a given number of iterations and at the end, we have our clusters.'''

# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[2]:


from sklearn.datasets import make_blobs


# In[3]:


data=make_blobs(n_samples=400, n_features=2,centers=4, cluster_std=2.0, random_state=101)


# In[4]:


from sklearn.cluster import KMeans


# In[5]:


data[1]


# In[6]:


df=pd.DataFrame(data[0])


# In[7]:


df.describe()


# In[8]:


df.head()


# In[9]:


df.plot.scatter(0,1,c=data[1],cmap='rainbow')


# In[10]:


model=KMeans(n_clusters=4).fit(df)


# In[11]:


model.labels_


# In[12]:


df.plot.scatter(0,1,c=model.labels_,cmap='rainbow')


# In[13]:


plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.scatter(df[0],df[1],c=data[1],cmap='copper')
plt.title('Original')
plt.grid()
plt.subplot(1,2,2)
plt.scatter(df[0],df[1],c=model.labels_,cmap='plasma')
plt.title('Clustered')
plt.grid()

