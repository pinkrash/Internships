#!/usr/bin/env python
# coding: utf-8

# # WEB SCRAPING USING BEAUTIFUL SOUP

# In[1]:


from bs4 import BeautifulSoup
import requests



# In[ ]:


# 1) Write a python program to display all the header tags from wikipedia.org and make data frame.


# In[3]:


page1=requests.get('https://wikipedia.org')
page1


# In[4]:


soup1=BeautifulSoup(page1.content)
soup1


# In[5]:


headers=[]
for i in soup1.find_all(['h1','h2','h3','h4','h5','h6']):
    headers.append(i.text)


# In[6]:


headers


# In[15]:


import pandas as pd


# In[121]:


df=pd.DataFrame(headers,columns=['tags'])
df


# In[ ]:


# 2) Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice)
from https://presidentofindia.nic.in/former-presidents.htm and make data frame.


# In[8]:


page2=requests.get('https://presidentofindia.nic.in/former-presidents')
page2


# In[9]:


soup2=BeautifulSoup(page2.content)
soup2


# In[13]:


presidents=[]
for i in soup2.find_all('div',class_="desc-sec"):
    presidents.append(i.text.replace('\n',''))


# In[14]:


presidents


# In[20]:


df=pd.DataFrame(presidents,columns=['president/chronological order'])
df


# In[ ]:


# 3) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame.


# In[22]:


page3=requests.get('https://www.icc-cricket.com/rankings/team-rankings/mens/odi')
page3


# In[23]:


soup3=BeautifulSoup(page3.content)
soup3


# In[ ]:


# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.


# In[125]:


ODI_team=[]
for i in soup3.find_all('h3',class_="si-team-name"):
    ODI_team.append(i.text)
    


# In[126]:


ODI_team


# In[ ]:


# Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame.


# In[50]:


import re
page5=requests.get(' https://www.cnbc.com/world/?region=world')
page5


# In[51]:


soup5=BeautifulSoup(page5.content)
soup5


# In[52]:


time=[]
for i in soup5.find_all('span',class_="LatestNews-wrapper"):
    time.append(i.text)


# In[53]:


time


# In[54]:


latest_news=[]
for i in soup5.find_all('div',class_="LatestNews-headlineWrapper"):
    latest_news.append(i.text)
    
                        


# In[55]:


latest_news


# In[130]:


news_link=[]
for link in soup5.find_all('a',class_="LatestNews-headline"):
    news_link.append(link['href'])
     


# In[131]:


news_link


# In[135]:


DF=pd.DataFrame({'latest_news':latest_news,'time':time,'URL':news_link})
DF


# In[ ]:


# 6) Write a python program to scrape the details of most downloaded articles from AI in last 90
days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
Scrape below mentioned details and make data frame


# In[71]:


page6=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page6


# In[72]:


soup6=BeautifulSoup(page6.content)
soup6


# In[77]:


paper_title=[]
for i in soup6.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    paper_title.append(i.text)


# In[78]:


paper_title


# In[79]:


authors=[]
for i in soup6.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    authors.append(i.text)


# In[80]:


authors


# In[83]:


published_date=[]
for i in soup6.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    published_date.append(i.text)


# In[84]:


published_date


# In[136]:


URL=[]
for i in soup6.find_all('a',class_="sc-5smygv-0 fIXTHm"):
    URL.append(i['href'])


# In[137]:


URL


# In[139]:


df=pd.DataFrame({'paper_titles':paper_title,'Authors':authors,'Published_Date':published_date,'Paper_URL':URL})
df
                 


# In[ ]:


# 7) Write a python program to scrape mentioned details from dineout.co.in and make data frame


# In[102]:


page7=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page7


# In[103]:


soup7=BeautifulSoup(page7.content)


# In[104]:


soup7


# In[105]:


restaurant_name=[]

for i in soup7.find_all('div',class_="restnt-info cursor"):
    restaurant_name.append(i.text)


# In[106]:


restaurant_name


# In[107]:


cuisine=[]
for i in soup7.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text)


# In[108]:


cuisine


# In[110]:


location=[]
for i in soup7.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)


# In[111]:


location


# In[112]:


rating=[]
for i in soup7.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)


# In[113]:


rating


# In[114]:


img_URL=[]
for i in soup7.find_all('img',"no-img"):
    img_URL.append(i['data-src'])


# In[115]:


img_URL


# In[119]:


df=pd.DataFrame({'Restaurant Name':restaurant_name,'Cuisine':cuisine,'Location':location,'Rating':rating,  "IMG-URL":img_URL})


# In[120]:


df


# In[ ]:




