
# coding: utf-8

# # BeautifulSoup(WebScrapping)

# BeautifulSoup is used to scrap data from online pages, sites. There are times when data is readily available in such time we require web scrapping. The biggest example of a company using this is Trivago( this app generates a comparision of alll other apps that are renting rooms).

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url='https://www.google.com/search?q=tanvi'#an example to get url from whereever you want to get data.


# In[3]:


r = requests.get(url)


# In[4]:


r.status_code #checks with acssesibility. It should be 200. If is above then it means there are restrictions of availing the data.


# In[8]:


url2 = 'https://pythonhow.com/example.html'


# In[9]:


head = {'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
}


# In[10]:


r2 = requests.get(url2,headers=head)


# In[7]:


r2.status_code


# In[12]:


r2.status_code


# In[14]:


print(r2.text)


# In[15]:


soup = BeautifulSoup(r2.text,'html.parser')


# In[16]:


cityName = soup.find_all('h2') #we find all the names that are in heading 2, in such way we find out the place the data is located.


# In[17]:


cityName


# In[18]:


descs = soup.find_all('p')


# In[19]:


descs


# In[20]:


cityName[0]


# In[21]:


cityName[0].text


# In[22]:


cityName


# In[28]:


s1 = soup.find_all('div',{'class':'cities'})


# In[29]:


s1


# In[23]:


d = {'city' : [i.text for i in soup.find_all('h2')],
        'desc' : [i.text for i in soup.find_all('p')]}#after scarpping the data we need to organize it.


# In[24]:


d


# In[25]:


import pandas as pd


# In[26]:


df = pd.DataFrame(d)


# In[27]:


df


# In[30]:


url3 = 'https://www.flipkart.com/search?q=fossil+watch&page=1'# Similarly we can do this with flipkart, here I tried to scrap watches and about them.


# In[31]:


r3 = requests.get(url3,headers=head)


# In[32]:


r3.status_code


# In[33]:


soup3 = BeautifulSoup(r3.text,'html.parser')


# In[35]:


Watchname = soup3.find_all('a',{'class':'_2cLu-l'})


# In[36]:


Names = [i.text for i in soup3.find_all('a',{'class':'_2cLu-l'})]


# In[39]:


df2 = pd.DataFrame({'Names':Names})
df2.head()


# In[49]:


df2['Gender'] = df2['Names'].apply(lambda x: 'Women' if 'women' in x.lower() else 'Men')


# In[50]:


df2.head()

