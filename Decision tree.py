#Decision Tree creates as model or  a tree visualization. It makes model of decisions with number of possible consequences.  
# coding: utf-8

# In[5]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[6]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


# In[9]:


df=pd.read_csv(r'C:\Users\tanvi\Desktop\python classes\ML\advertising.csv')


# In[10]:


df.head()


# In[11]:


df.columns


# In[12]:


df.info()


# In[13]:


sns.pairplot(df)


# In[14]:



df.columns


# In[15]:


x=df[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage']]
y=df['Clicked on Ad']


# In[16]:


df.info()


# In[17]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=101)


# In[18]:


model = DecisionTreeClassifier().fit(x_train,y_train)


# In[19]:


pred = model.predict(x_test)


# In[20]:


from sklearn.metrics import classification_report, confusion_matrix


# In[21]:


print(classification_report(y_test,pred))
print(confusion_matrix(y_test,pred))


# In[22]:


from IPython.display import Image


# In[23]:


from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz


# In[24]:


dd=StringIO()


# In[25]:


export_graphviz(model, out_file=dd, feature_names=x.columns,filled=True, rounded=True)


# In[26]:


import pydot


# In[27]:


graph=pydot.graph_from_dot_data(dd.getvalue())


# In[31]:


g0=graph[0]


# In[33]:


Image(graph[0].create_png())

