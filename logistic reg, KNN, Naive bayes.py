
# coding: utf-8

# # Logistic Regression,Bayes Theorm,KNeighborsClassifier Desicion Tree
'''Logistic Regression: Logistic regression is used to describe data and to explain the relationship between one dependent binary variable and one or more nominal, ordinal, interval or ratio-level independent variables.
   It is a predictive analysis'''
'''Bayes theorm: It is known as naive bayes. It assumes that the presence of a particular feature in a class is unrelated to the presence of any other feature '''
'''KNeighborsClassifier: In pattern recognition, the k-nearest neighbors algorithm (k-NN) is a non-parametric method used for classification and regression.The output depends on whether k-NN is used for classification or regression: In k-NN classification, the output is a class membership '''
# In[4]:


import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df=pd.read_csv(r'C:\Users\tanvi\Desktop\python classes\ML\advertising.csv')


# In[6]:


df.head()


# ## Logistic Regression

# In[8]:


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
df.columns


# In[9]:


x=df[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage']]
y=df['Clicked on Ad']


# In[12]:


x_train , x_test, y_train, y_test= train_test_split(x,y,test_size=0.3, random_state=101)


# In[13]:


model=LogisticRegression().fit(x_train, y_train)


# In[14]:


pred=model.predict(x_test)


# In[15]:


from sklearn.metrics import classification_report, confusion_matrix


# In[16]:


print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))


# In[18]:


model.score(x_train, y_train)


# In[19]:


model.score(x_test, y_test)


# In[20]:


from sklearn.metrics import mean_squared_error, mean_absolute_error


# In[21]:


print(mean_absolute_error(y_test, pred))


# In[22]:


print(mean_squared_error(y_test, pred))


# KNN

# In[23]:


from sklearn.neighbors import KNeighborsClassifier


# In[24]:


model1= KNeighborsClassifier(n_neighbors=4).fit(x_train, y_train)


# In[25]:


err = []
err1 = []
for i in range(1,int(len(x_train)*0.3),2):
    mod = KNeighborsClassifier(n_neighbors=i).fit(x_train, y_train)
    pred = mod.predict(x_test)
    err.append(np.mean(pred!=y_test))
    err1.append(1-(mod.score(x_test,y_test)))


# In[51]:


plt.figure(figsize=(12,8))
plt.plot(range(1,int(len(x_train)*0.3),2),err,ls='--',marker='o',markersize=10,lw=3,markerfacecolor='red')
plt.grid()
plt.xlabel('Number of Neighbors --->')
plt.ylabel('Errors --->')
plt.title('N_neighbors versus Error Graph')

mod.score(x_test, y_test)


# In[31]:


from sklearn.model_selection import GridSearchCV
grid=GridSearchCV(SVC(),param_grid={'c':1,20,30,50,60,70,100,130,150})    


# In[38]:


from sklearn.tree import DecisionTreeClassifier


# In[39]:


mod_d=DecisionTreeClassifier().fit(x_train, y_train)


# In[40]:


pre_d=mod_d.predict(x_test)


# In[41]:


print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))


# In[43]:


from IPython.display import Image
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
dd=StringIO()
export_graphviz(mod_d, out_file=dd, feature_names=x.columns,filled=True, rounded=True)
import pydot
graph=pydot.graph_from_dot_data(dd.getvalue())


# In[44]:


Image(graph[0].create_png())


# In[45]:


from sklearn.naive_bayes import BernoulliNB
model_bayes=BernoulliNB().fit(x_train, y_train)


# In[46]:


pred_bayes=model_bayes.predict(x_test)


# In[48]:


print(classification_report(y_test, pred_bayes))
print(confusion_matrix(y_test, pred_bayes))

