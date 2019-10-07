
# coding: utf-8

# # Pandas 

# In[1]:


import pandas as pd


# In[2]:


df = pd.DataFrame({'a':['Apple',
                        'This is something',
                        '   and this is another one         ',
                        'or you can? NO I can not',
                        'Nice',
                        'applies']})


# In[3]:


df1 = pd.DataFrame({'Attendance':list('APPPPPAAAPPPPPPPPAPAPAPPPPAAPPPPPA')}) #how do we check with absenties in a class


# In[4]:


df1['Attendance'].value_counts()


# In[5]:


df1['Attendance'].size


# In[6]:


df1['Attendance'].nunique()


# #get_dummies is usefull when we need to classify the data in groups. If we have have n categories, then we should make n-1 number of dummies. This procedure is widely used in regression.

# In[7]:


pd.get_dummies(df1['Attendance']).head(2)


# In[8]:


pd.get_dummies(df1['Attendance'],drop_first=True).head()


# In[9]:


df1 = pd.DataFrame({'name':['Tanvi','Parul','Gauri','Atul'],
                   'age':[23,21,22,23],
                   'id':[1,2,4,3]})
df2 = pd.DataFrame({'id':[2,4,1,5,6],
                   'salary':[3000,3400,2300,8790,4500],
                   'experience':[2,3,1,6,4]})


# In[10]:


pd.merge(df1,df2,on='id')


# In[11]:


pd.merge(df1,df2,on='id',how='inner')


# In[12]:


pd.merge(df1,df2,on='id',how='outer')


# In[13]:


pd.merge(df1,df2,on='id',how='left')


# In[14]:


pd.merge(df1,df2,on='id',how='right')


# In[15]:


df1


# In[17]:


df11 = pd.DataFrame({'name':['Tanvi','Parul','Kushagra','Ravya'],
                   'age':[23,29,21,22],
                   'id':[7,8,10,13],
                    'exp':[3,2,8,1]})


# In[18]:


pd.concat([df1,df11],axis=0)


# In[19]:


df1.join(df2,on='id',lsuffix='_c')


# In[20]:


import numpy as np


# In[21]:


df = pd.DataFrame({'a':[23,6,478,456,88],
                  'b':[54,8,np.nan,np.nan,46],
                  'c':[23,np.nan,np.nan,4,5]})


# In[22]:


df


# In[23]:


pd.isnull(df)


# In[24]:


df.dropna()


# In[25]:


import pandas as pd


# In[26]:


df.dropna(axis=1)


# In[27]:


df['b'].dropna()


# In[28]:


df.dropna(thresh=1)


# In[29]:


df.dropna(thresh=2)


# In[31]:


df.fillna('0')


# In[32]:


df['b'].fillna(df['b'].mean())


# In[33]:


df['b'].fillna(df['b'].mean(),inplace=True)


# In[34]:


df


# In[35]:


df.drop(['a','b'],axis=1)


# In[36]:


df = pd.DataFrame({'Name':['John','Riddhi','Sam','Arun','Rohan','Rahul','Wright'],
                  'Company':['Microsoft','Microsoft','Google','Google','TCS','TCS','Google'],
                  'Salary':[65000,45000,4000,9000,9500,90000,8000],
                  'YearOfJoin':[2010,2010,2013,2013,2015,2016,2014],
                  'Experience':[9,9,6,6,4,3,3]})


# In[37]:


df


# In[38]:


df.groupby('Company')['Salary'].mean()['Microsoft']


# In[39]:


df.groupby('Company')['Salary'].mean()


# In[40]:


df.columns


# In[41]:


df[['Company','Name']].describe()


# In[43]:


df.groupby('Company').describe().T


# In[44]:


df.groupby('YearOfJoin').describe().T


# In[45]:


df.groupby(['Company','YearOfJoin']).mean()


# In[46]:


df.groupby(['Company','YearOfJoin']).max()


# In[47]:


df.groupby(['Company','YearOfJoin']).groups


# In[48]:


# df


# In[49]:


df.groupby(['Company','YearOfJoin']).get_group(('Google',2013))


# In[50]:


g = df.groupby(['Company','YearOfJoin'])


# In[51]:


g.transform(lambda x:x.mean())


# In[52]:


g.agg(['mean','min','std','var'])

