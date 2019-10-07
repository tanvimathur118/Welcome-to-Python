
# coding: utf-8

# # Natural Language processing

# This processing tries to bridge a gap between the human and computer by letting computer understand what humans are saying. Simplest example : Gmail classifies the mail into categories, So how do they understand the which mail is spam and which not. To classify this NLP or NLPK are used. 

# In[2]:


import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df=pd.read_csv(r'C:\Users\tanvi\Desktop\python classes\ML\smsspamcollection\SMSSpamCollection',sep='\t',names=['type','msg'])


# In[7]:


df.head()


# In[8]:


df.describe()


# In[57]:


df.info()


# In[9]:


df['type'].describe()


# In[10]:


df.head()


# In[11]:


df['msg'].value_counts()


# In[12]:


df.groupby('type').describe()


# In[13]:


new_type=pd.get_dummies(df['type'])


# In[14]:


df = pd.concat([df,new_type],axis=1)


# In[15]:


df.head()


# In[16]:


df['ham'].value_counts()


# In[17]:


df['spam'].value_counts()


# In[18]:


df


# In[19]:


sns.heatmap(pd.isnull(df))


# We check with some words punctuations that are not needed to indentify. There are some words already listed.

# In[38]:


from nltk.corpus import stopwords as sw
from string import punctuation as punc


# In[22]:


df['len']=df['msg'].apply(len)


# In[92]:


df.head()


# In[23]:


sns.distplot(df['len'][df['type']=='ham'],)


# In[24]:


sns.distplot(df['len'][df['type']=='spam'],)


# In[39]:


import nltk


# In[40]:


nltk.download('stopwords')


# In[41]:


sw.words('english')


# In[27]:


df['msg'][10]


# In[43]:


punc


# In[44]:


swe=sw.words('english')


# In[45]:


def text_process(t):
    t = t.lower()
    print(t)
    t = ' '.join([i for i in t.split() if i not in swe])
    print(t)
    t = ''.join([i for i in t if i not in punc])
    print(t)
    t = [i for i in t.split() if i not in swe]
    print(t)
    return t  ## this will depend on the complexity of the string you have.


# In[46]:


k=df['msg'][10]


# In[47]:


type(k)


# In[48]:


nn=text_process(k)


# In[49]:


from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

#these are important to generate a model


# In[52]:


x_train, x_test, y_train, y_test=train_test_split(df['msg'],df['type'], test_size=0.3, random_state=101)


# In[56]:


model=Pipeline([('cv', CountVectorizer(text_process)),('tfidf',TfidfTransformer()),('mb', MultinomialNB())]).fit(x_train, y_train)


# In[57]:


pred=model.predict(x_test)


# In[58]:


print(model.score(x_test, y_test))


# In[59]:


print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))


# ##The avg f1-score is pretty good, thereby we accpet this model.##
