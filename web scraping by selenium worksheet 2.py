#!/usr/bin/env python
# coding: utf-8

# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# #Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
# jobs data.
# 

# In[50]:


driver=webdriver.Chrome()


# In[51]:


driver.get(' https://www.shine.com')


# In[55]:


job_title=driver.find_element(By.CLASS_NAME,'form-control ')
job_title.send_keys('Data Analyst')


# In[56]:


location=driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input')
location.send_keys('Bangalore')


# In[57]:


search=driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button')
search.click()


# In[58]:


Job_Title=[]
Job_location=[]
Company_name=[]
Experience_required=[]


# In[59]:


title=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]/a')
for i in title:
    Job_Title.append(i.text)


# In[89]:


A=Job_Title[:10]
A


# In[90]:


loc=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists__fdnsc"]/div[2]')
for i in loc:
    Job_location.append(i.text)
    
B=Job_location[:10]
B


# In[91]:


company=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company:
    Company_name.append(i.text)
    
C=Company_name[:10]
C
    


# In[92]:


exp=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists__fdnsc"]/div[1]')
for i in exp:
    Experience_required.append(i.text)
    
D=Experience_required[:10]
D


# In[93]:


print(len(A))
print(len(B))
print(len(C))
print(len(D))


# In[96]:


DF=pd.DataFrame({'Job_Title':A,"Job_location":B,'Company_name':C,'Experience_required':D})
DF


# #Q2:Write a python program to scrape data for “Data Scientist” Job position in“Bangalore” location. You
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# 

# In[126]:


driver=webdriver.Chrome()


# In[127]:


driver.get('https://www.shine.com/')


# In[129]:


title=driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/input')
title.send_keys('Data Scientist')


# In[130]:


location=driver.find_element(By.NAME,'id_loc')
location.send_keys('Bangalore')


# In[131]:


search=driver.find_element(By.CLASS_NAME,'searchForm_btnWrap__Cb75F')
search.click()


# In[132]:


job_title=[]
job=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]/a')
for i in job:
    job_title.append(i.text)


# In[149]:


E=job_title[:10]
E


# In[140]:


job_location=[]
loc=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists__fdnsc"]/div[2]')
for i in loc:
    job_location.append(i.text)


# In[150]:


F=job_location[:10]
F


# In[142]:


company_name=[]
company=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company:
    company_name.append(i.text)


# In[151]:


G=company_name[:10]
G


# In[145]:


experience_required=[]
exp=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists__fdnsc"]/div[1]')
for i in exp:
    experience_required.append(i.text)


# In[152]:


H=experience_required[:10]
H


# In[153]:


df=pd.DataFrame({'job title':E,"job location":F,'company':G,'experience required':H})


# In[154]:


df


# Q3: In this question you have to scrape data using the filters available on the webpage
#  You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs

# In[175]:


driver=webdriver.Chrome()


# In[176]:


driver.get('https://www.shine.com')


# In[180]:


designation=driver.find_element(By.CLASS_NAME,'form-control')
designation.send_keys('Data Scientist')


# In[181]:


search=driver.find_element(By.CLASS_NAME,'searchForm_btnWrap__Cb75F')
search.click()


# In[182]:


locations=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]/div/div[1]/div/div[2]/div/ul/li[1]/button')
locations.send_keys('Delhi/NCR')


# In[188]:


salary=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]/div/div[1]/div/div[2]/div/ul/li[3]/button')
salary.send_keys('3 to 6 lakhs')


# In[189]:


show_result=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div[4]/button[2]')
show_result.click()


# In[191]:


TITLE=[]
title=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title:
    TITLE.append(i.text)
    
I=TITLE[:10]


# In[192]:


I


# In[195]:


company=[]
comp=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in comp:
    company.append(i.text)
    
J=company[:10]


# In[196]:


J


# In[203]:


location=[]
Loc=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists__fdnsc"]/div[2]')
for i in Loc:
    location.append(i.text)
    
K=location[:10]


# In[204]:


K


# In[215]:


experience=[]
EXP=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists__fdnsc"]/div[1]')
for i in EXP:
    experience.append(i.text)
    
L=experience[:10]


# In[216]:


L


# In[217]:


df=pd.DataFrame({'job title':I,'company name':J,'location':K,'experience requirment':L})
df


# Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
#  Brand
#  ProductDescription
#  Price
# The attributes which you have to scrape is ticked marked in the below image.

# In[218]:


driver=webdriver.Chrome()


# In[221]:


driver.get('https://www.flipkart.com/')


# In[226]:


product=driver.find_element(By.CLASS_NAME,'Pke_EE')
product.send_keys('sunglasses')


# In[227]:


search=driver.find_element(By.CLASS_NAME,'_2iLD__')
search.click()


# In[233]:


BRAND=[]


# In[234]:


start=0
end=3
for page in range(start,end):
    brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand:
        BRAND.append(i.text)
next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]') 
next_button.click()
time.sleep(3)
    


# In[235]:


BRAND


# In[237]:


A=BRAND[:100]
A


# In[238]:


Product_Description=[]


# In[239]:


start=0
end=3
for page in range(start,end):
    description=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in description:
        Product_Description.append(i.text)
next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]') 
next_button.click()
time.sleep(3)


# In[240]:


B=Product_Description[:100]
B


# In[244]:


Price=[]


# In[246]:


start=0
end=3
for page in range(start,end):
    rate=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in rate:
        Price.append(i.text)
next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]') 
next_button.click()
time.sleep(3)


# In[247]:


C=Price[:100]
C


# In[248]:


Offer=[]


# In[249]:


start=0
end=3
for page in range(start,end):
    off=driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
    for i in off:
        Offer.append(i.text)
next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]') 
next_button.click()
time.sleep(3)


# In[250]:


D=Offer[:100]
D


# In[251]:


df=pd.DataFrame({'Brand':A,'Product Description':B,'Price':C,'Offer':D})
df


# Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market
# place=FLIPKART

# In[81]:


driver=webdriver.Chrome()


# In[82]:


driver.get(' https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market place=FLIPKART')


# In[83]:


home_page=driver.find_element(By.CLASS_NAME,'button')
home_page.click()


# In[84]:


product=driver.find_element(By.CLASS_NAME,'Pke_EE')
product.send_keys('iPhone 11 black 64 GB')


# In[85]:


search=driver.find_element(By.CLASS_NAME,"_2iLD__")
search.click()


# In[86]:


details=driver.find_element(By.CLASS_NAME,'_2kHMtA')
details.click()


# In[101]:


ratings=[]

    
rate=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
for i in rate:
    ratings.append(i.text)
   


# In[102]:


ratings


# In[89]:


review_summary=[]
review=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in review:
    review_summary.append(i.text)


# In[90]:


review_summary


# In[93]:


full_review=[]


# In[94]:


full=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in full:
    full_review.append(i.text)


# In[95]:


full_review


# In[59]:


df=pd.DataFrame({'ratings':ratings,'review':review_summary,'full_review':full_review})
df


# #Q6: Scrape data forfirst 100 sneakers you find whenyou visit flipkart.com and search for “sneakers” inthe
# search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price
# 

# In[387]:


driver=webdriver.Chrome()


# In[391]:


driver.get('https://flipkart.com')


# In[392]:


product=driver.find_element(By.CLASS_NAME,'Pke_EE')
product.send_keys('sneakers')


# In[393]:


search=driver.find_element(By.CLASS_NAME,'_2iLD__')
search.click()


# In[397]:


BRAND=[]


# In[399]:


for i in range(0,3):
    brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand:
        BRAND.append(i.text)
next_button=driver.find_element(By.CLASS_NAME,'_1LKTO3')
next_button.click()


# In[403]:


Brand=BRAND[:100]
Brand


# In[404]:


len(Brand)


# In[405]:


Description=[]
for i in range(0,3):
    
    description=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in description:
        Description.append(i.text)
next_button=driver.find_element(By.CLASS_NAME,'_1LKTO3')
next_button.click()


# In[406]:


details=Description[:100]
details


# In[407]:


len(details)


# In[409]:


price=[]
for i in range(0,3):
    rate=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in rate:
        price.append(i.text)

next_button=driver.find_element(By.CLASS_NAME,'_1LKTO3')
next_button.click()
        


# In[410]:


Price=price[:100]
Price


# In[411]:


df=pd.DataFrame({'brand':Brand,'Details':details,'price':Price})
df


# #Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then
# set CPU Type filter to “Intel Core i7” as shown in the below image:

# #After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[27]:


driver=webdriver.Chrome()


# In[28]:


driver.get(" https://www.amazon.in/ ")


# In[29]:


product=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
product.send_keys('laptop')


# In[30]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search.click()


# In[31]:


CPU=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[19]/span/span[9]/li/span/a/div/label/i')
CPU.click()


# In[32]:


Laptop=[]
laptop=driver.find_elements(By.XPATH,'//span[@class="a-size-base-plus a-color-base"]')
for i in laptop:
    Laptop.append(i.text)


# In[33]:


x=Laptop[:10]
x


# In[49]:


rating=[]
rates=driver.find_elements(By.XPATH,'//i[@class="a-icon a-icon-popover"]')
for i in rates:
    rating.append(i.text)


# In[50]:


y=rating[:10]
y


# In[51]:


price=[]
cost=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in cost:
    price.append(i.text)


# In[52]:


z=price[:10]
z


# In[53]:


df=pd.DataFrame({'title':x,'rating':y,'price':z})
df


# #Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on TopQuote
# 3. Than scrap a) Quote b) Author c) Type Of Quotes

# In[54]:


driver=webdriver.Chrome()


# In[55]:


driver.get('https://www.azquotes.com')


# In[56]:


top_quotes=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
top_quotes.click()


# In[57]:


Quote=[]
for page in range(0,10):
    quote=driver.find_elements(By.XPATH,'//a[@class="title"]')
    for i in quote:
        Quote.append(i.text)
next_page=driver.find_element(By.CLASS_NAME,'next')
next_page.click()
    


# In[58]:


Quote


# In[47]:


len(Quote)


# In[55]:


Author=[]
for page in range(0,10):
    author=driver.find_elements(By.XPATH,'//div[@class="author"]')
    for i in author:
        Author.append(i.text)
next_button=driver.find_element(By.CLASS_NAME,'next')
next_button.click()    


# In[56]:


Author


# In[50]:


len(Author)


# In[51]:


Type_of_quotes=[]
for page in range(0,10):
    typo=driver.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in typo:
        Type_of_quotes.append(i.text)
next_button=driver.find_element(By.CLASS_NAME,'next')
next_button.click()


# In[52]:


Type_of_quotes


# In[26]:


len(Type_of_quotes)


# In[57]:


df=pd.DataFrame({'Quotes':Quote,'Authors':Author,'Typo of quotes':Type_of_quotes})
df


# #Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead,
# Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpagehttps://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make theDataFrame

# In[104]:


driver=webdriver.Chrome()


# In[105]:


driver.get('https://www.jagranjosh.com/')


# In[106]:


GK=driver.find_element(By.XPATH,'/html/body/div/header/nav/div/div/div[3]/ul/li[3]/a')
GK.click()


# In[110]:


Primeministers=driver.find_element(By.XPATH,'/html/body/div[1]/div[8]/section[8]/div/ul/li[10]/a')
Primeministers.click()


# In[121]:


List_Of_Primeministers=[]

table_body=driver.find_element(By.XPATH,'/html/body/div[1]/main/div[1]/div[1]/article/div[4]/div[7]/div/table/tbody')
table_rows=table_body.find_elements(By.TAG_NAME,'tr')
for rows in table_rows:
    k=rows.text
    table_data=rows.find_elements(By.CSS_SELECTOR,'td,th')
    
    for data in table_data:
        List_Of_Primeministers.append(data.text)
List_Of_Primeministers
    
  


# In[125]:


df=pd.DataFrame(List_Of_Primeministers)
df


# #Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e.
# Car name and Price) from https://www.motor1.com

# In[60]:


driver=webdriver.Chrome()


# In[61]:


driver.get('https://www.motor1.com')


# In[64]:


most_expensive_cars=driver.find_element(By.XPATH,'/html/body/div[10]/div[9]/div/div[1]/div/div/div[2]/div/div[1]/h3/a')
most_expensive_cars.click()


# In[65]:


Name=[]
name=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in name:
    Name.append(i.text)
    


# In[78]:


name=Name[:50]
name


# In[69]:


price=[]
p=driver.find_elements(By.TAG_NAME,'strong')
for i in p:
    price.append(i.text)


# In[79]:


price


# In[80]:


df=pd.DataFrame({'NAME':name,'PRICE':price})
df


# In[ ]:




