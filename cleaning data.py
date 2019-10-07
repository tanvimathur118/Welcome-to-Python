
# coding: utf-8
##Cleaning data is an essential step before analyzing the data. To clean means we remove values not needed, duplicate values, break down infomation that we need into rows and columns.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


get_ipython().system('file billboard')


# In[8]:


billboard=pd.read_csv(r'C:\Users\tanvi\Desktop\billboard.csv', encoding='latin-1')


# In[9]:


billboard.head()


# In[10]:


billboard.columns


# In[12]:


plt.plot(billboard.loc[0,'x1st.week':'x76th.week'])


# In[13]:


plt.plot(range(1,77),billboard.loc[0,'x1st.week':'x76th.week'])


# In[23]:


for index, row in billboard.iterrows():
    plt.plot(range(1,77),row['x1st.week':'x76th.week'],color='blue', alpha=0.1)


# In[24]:


bshort=billboard[['artist.inverted','track','time','date.entered','x1st.week','x2nd.week','x3rd.week']]


# In[25]:


bshort.head()


# In[26]:


bshort.columns=['artist','track','time','date.entered','wk1','wk2','wk3']


# In[27]:


bshort.head()


# In[28]:


bmelt=bshort.melt(['artist','track','time','date.entered'],['wk1','wk2','wk3'],'week','rank')


# In[29]:


bmelt.head()


# In[31]:


bmelt.query('track == "Liar"')


# In[36]:


bmelt['week']=bmelt['week'].apply(lambda s:int(s[2]))


# In[37]:


bmelt['date.entered']=pd.to_datetime(bmelt['date.entered'])


# In[38]:


bmelt['date.entered'][0]+pd.Timedelta('7 days')


# In[39]:


bmelt['date']=bmelt['date.entered']+pd.Timedelta('7 days')*(bmelt['week']-1)


# In[46]:


bfinal.head()


# bmelt.drop([

# In[41]:


bmelt.drop(['date.entered'],axis=1, inplace= True)


# In[43]:


bfinal=bmelt[['artist','track','time','date','week','rank']]


# In[45]:


bfinal.head()
bfinal.sort_values(['artist','track'], inplace=True)


# In[47]:


tracks=bfinal[['artist','track','time']].drop_duplicates()


# In[48]:


tracks.head()


# In[49]:


tracks.index.name='id'
tracksid=tracks.reset_index()
tracksid.head()


# In[51]:


pd.merge(tracksid, bfinal, on=['track','artist','time']).head()


# In[53]:


tb=pd.read_csv(r'C:\Users\tanvi\Desktop\Ex_Files_Python_Statistics_EssT\Exercise Files\chapter2\02_05\tb.csv')


# In[54]:


tb.head()


# In[56]:


tb.columns


# In[57]:


melted=tb.melt(['country', 'year'],['m04', 'm514', 'm014', 'm1524', 'm2534', 'm3544','m4554', 'm5564', 'm65', 'mu', 'f04', 'f514', 'f014', 'f1524', 'f2534','f3544', 'f4554', 'f5564', 'f65', 'fu'],'sexage','cases')


# In[59]:


melted.head()


# In[60]:


melted['sex']=melted['sexage'].str.slice(0,1)
melted['age']=melted['sexage'].str.slice(1)


# In[67]:


melted.head(5)


# In[62]:


melted .drop(['sexage'], axis=1, inplace=True)


# In[66]:


melted['age']=melted['age'].map({'04':'0-4','514':'5-14','1524':'15-24','2534':'25-34','3544':'35-44','4454':'44-54','5564':'55-64','65':'65+','u':np.nan})


# In[68]:


final=melted.dropna(subset=['cases'])


# In[71]:


final.head()


# In[72]:


final.sort_values(['country','year','age','sex'])
final.head()


# In[73]:


final[['country','year','age','sex','cases']]

