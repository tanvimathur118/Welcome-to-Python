#Exploring the different graphs using Matplotlib
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


import numpy as np


# In[21]:


x=np.arange(1,20)
y=x**2
y1 = x**3
plt.plot(x,y)
plt.plot(x,y1)
plt.xlabel('x -->')
plt.ylabel('y-->')
plt.title('My Graph')
plt.grid()
plt.legend(['y wala','y1 wala'])


# In[37]:


plt.figure(figsize=(15,8))
plt.subplot(2,1,1)
plt.plot(x,y,ls='-.',color='red',lw=5,marker='o',markersize=10,markerfacecolor='blue',markeredgecolor='blue')
plt.title('First')
plt.subplot(2,1,2)
plt.plot(x,y1,ls='--',lw=3)
plt.title('Second')
plt.grid()


# In[13]:


plt.bar(x,y)


# In[4]:


#bar
x=[2,5,8,9,6]
y=[5,4,6,2,9]
plt.bar(x,y)
plt.show()


# In[5]:


#hist


# In[7]:


x=[2,6,9,5]
plt.hist(x)
plt.show()


# In[38]:


import pandas as pd
import seaborn as sns


# In[39]:


df1 = sns.load_dataset('tips')
df2 = sns.load_dataset('iris')
df3 = sns.load_dataset('flights')


# In[40]:


df1.head()


# In[41]:


df1.info()


# In[42]:


df1.describe()


# In[43]:


df1[['sex','smoker','day','time']].describe()


# In[44]:


df1['sex'].value_counts()


# In[45]:


df1['time'].value_counts()


# In[47]:


df1['day'].value_counts()


# In[48]:


df1['smoker'].value_counts()


# In[50]:


df1.groupby('sex').describe().T


# In[51]:


df1['total_bill'].plot()


# In[53]:


df1['total_bill'].plot.hist(bins=30)


# In[55]:


df1.plot.scatter('total_bill','tip')


# In[56]:


sns.countplot(x='sex',data=df1)


# In[57]:


sns.countplot(x='sex',data=df1,hue='smoker')


# In[58]:


sns.countplot(x='sex',data=df1,hue='day')


# In[61]:


sns.countplot(x='sex',data=df1,hue='time',palette='Spectral')


# In[64]:


sns.barplot(x='sex',y='total_bill',data=df1,estimator=np.std,hue='smoker')


# In[ ]:


sns.violinplot(x='smoker',y='total_bill',data=df1)


# In[66]:


sns.violinplot(x='smoker',y='total_bill',data=df1)


# In[67]:


sns.violinplot(x='smoker',y='total_bill',data=df1,hue='sex')


# In[68]:


sns.violinplot(x='smoker',y='total_bill',data=df1,hue='sex',split=True)


# In[69]:


sns.stripplot(x='sex',y='total_bill',data=df1)


# In[70]:


sns.stripplot(x='sex',y='total_bill',data=df1,jitter=True)


# In[73]:


plt.figure(figsize=(10,7))
sns.boxplot(x='sex',y='total_bill',data=df1,hue='day')


# In[76]:


import warnings
warnings.filterwarnings('ignore')


# In[77]:


sns.distplot(df1['total_bill'])


# In[78]:


sns.jointplot(df1['total_bill'],df1['tip'])


# In[80]:


sns.jointplot(df1['total_bill'],df1['tip'],kind='hex',color='red')


# In[81]:


sns.jointplot(df1['total_bill'],df1['tip'],kind='kde')


# In[82]:


sns.pairplot(df1)


# In[83]:


sns.pairplot(df2)


# In[85]:


sns.kdeplot(df1['total_bill'])
sns.rugplot(df1['total_bill'])


# In[88]:


sns.lmplot('total_bill','tip',df1)


# In[89]:


df3.head()


# In[90]:


df31 = df3.pivot_table('passengers','year','month')
df31


# In[91]:


sns.heatmap(df31)


# In[92]:


sns.clustermap(df31)


# In[97]:


jg = sns.JointGrid('total_bill','tip',data=df1)
jg.plot(sns.regplot,sns.kdeplot)


# In[99]:


pg = sns.PairGrid(df1)
pg.map_diag(sns.kdeplot)
pg.map_lower(sns.kdeplot)
pg.map_upper(plt.scatter)


# In[111]:


fg = sns.FacetGrid(df1,row='sex',col='smoker',hue='day')
fg.map(plt.hist,'total_bill')

