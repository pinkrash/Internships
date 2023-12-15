#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

#1- Write a Python program to replace all occurrences of a space, comma, or dot with a
colon.
# In[14]:


text= 'Phython Exercises, PHP exercises.'
pattern= "[\s+.,]"
result= re.sub(pattern, ':', text)
print(result)

#2- Create a dataframe using the dictionary below and remove everything (commas (,), !,
XXXX, ;, etc.) from the columns except words.
# In[15]:


import pandas as pd


# In[17]:


dictionary={'SUMMARY':['hello, world!','XXXXX test', '123four,five:; six....']}
DATAFRAME= pd.DataFrame(dictionary)


# In[18]:


DATAFRAME


# In[688]:


x= "[,.!;:X+\d]"
y=DATAFRAME['SUMMARY'].str.replace(x," ")


# In[689]:


print(y)


# In[ ]:


#3- Create a function in python to find all words that are at least 4 characters long in a
string. The use of the re.compile() method is mandatory..


# In[38]:


words=re.compile("\w{4}")
def find_word(string):
    print (re.findall(words, string))
    


# In[39]:


find_word("this area is very fertile")


# In[ ]:


#4- Create a function in python to find all three, four, and five character words in a string.
The use of the re.compile() method is mandatory.


# In[40]:


w= re.compile("\w{3,5}")
def F (str):
    print (re.findall(w,str))


# In[41]:


F("there are too much heavy stones on the mountain")


# In[ ]:


#5- Create a function in Python to remove the parenthesis in a list of strings. The use of the
re.compile() method is mandatory.


# In[59]:


string=['example (.com)','hr@fliprobo (.com)','github (.com)','Hello (Data Science World)','Data (Scientist)']
A=re.compile(r'\(|\)')
for remove_p in string:
    P=A.sub('',remove_p)
    print(P)


# In[ ]:


#6- Write a python program to remove the parenthesis area from the text stored in the text
file using Regular Expression.


# In[73]:


with open ('file3') as T1:
    filetext=T1.read()
 


# In[74]:


filetext


# In[75]:


A= re.sub (r'\(|\)',"",filetext)
print(A)


# In[ ]:


#7- Write a regular expression in Python to split a string into uppercase letters.
Sample text: 'ImportanceOfRegularExpressionsInPython'


# In[691]:


string_text="ImportanceOfRegularExpressionsInPython"
split_text=re.findall(r'[A-Z]+[a-z]+', string_text)
print(split_text)


# In[ ]:


#8- Create a function in python to insert spaces between words starting with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
    


# In[611]:


def SPACE (TEXT):
    pattern='(?<!\b)(?=\d+)'
    newtext=re.sub(pattern," ",TEXT)
    print(newtext)


# In[612]:


SPACE('RegularExpression1IsAn2ImportantTopic3InPython')


# In[ ]:


#9- Create a function in python to insert spaces between words starting with capital letters
or with numbers.


# In[620]:


def space (txt):
     pattern='(?<!\b)(?=\d|[A-Z])'
     print(re.sub(pattern," ",txt))
  


# In[621]:


space("RegularExpression1IsAn2ImportantTopic3InPython")


# In[ ]:


#1010- Use the github link below to read the data and create a dataframe. After creating the
dataframe extract the first 6 letters of each country and store in the dataframe under a new column
called first_five_letters.


# In[88]:


import pandas as pd


# In[96]:


df=pd.read_csv('https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv')


# In[97]:


df


# In[104]:


df['Country'].str.extract(r'(^.{1,6})')


# In[ ]:


#11- Write a Python program to match a string that contains only upper and lowercase
letters, numbers, and underscores.


# In[700]:


def test(string):
    word_character=re.match(r'^\w+$',string)
    print(word_character)
                              
                              


# In[702]:


test('hello_123w')
test('hello Andrew')


# In[ ]:


#12. Write a Python program where a string will start with a specific number.


# In[373]:


def number (string):
    s=re.match('\d{3}',string)
    print(s)


# In[374]:


number('235 students are present in seminar.')


# In[ ]:


#13. Write a Python program to remove leading zeros from an IP address


# In[375]:


def remove_zero (IP_address):
    k=re.sub('[0]+','',IP_address)
    print(k)


# In[376]:


remove_zero("234.809.04.120")


# In[ ]:


#14- Write a regular expression in python to match a date string in the form of Month name
followed by day number and year stored in a text file.


# In[705]:


with open('TXT') as F:
    file_content=F.read()


# In[706]:


file_content


# In[707]:


pattern= r'((January|February|March|April|May|June|July|August|September|October|November|December)+\s+\w+\s+\d{4})'



# In[708]:


print(re.findall(pattern,file_content))


# In[494]:


print(re.search(pattern,file_content))


# In[ ]:


#15- Write a Python program to search some literals strings in a string.


# In[497]:


Tx='The quick brown fox jumps over the lazy dog.'
ptrn='fox|dog|horse'
print(re.findall(ptrn,Tx))


# In[ ]:


#16- Write a Python program to search a literals string in a string and also find the location
within the original string where the pattern occurs


# In[498]:


Tx='The quick brown fox jumps over the lazy dog.'
ptrn='fox'
print(re.search(ptrn,Tx))


# In[ ]:


#17-Write a Python program to find the substrings within a string.


# In[506]:


string=['Python exercises, PHP exercises, C# exercises.']

for STR in string:
    T='exercises'
    i=re.findall(T,STR)
    print(i)


# In[ ]:


#18- Write a Python program to find the occurrence and position of the substrings within a
string.


# In[520]:


string='Python exercises, PHP exercises, C# exercises.'
T='exercises'
i=re.finditer(T,string)
for obj in i:
    print(obj)


# In[ ]:


#19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy
format.


# In[ ]:


#20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a
string. The use of the re.compile() method is mandatory.


# In[559]:


def decimal (value):
    pattern=re.compile(r'\b\d+\.\d{1,2}\b')
    match=pattern.findall(value)
    print(match)


# In[560]:


decimal('01.12 0132.123 2.31875 145.8 3.01 27.25 0.25')


# In[ ]:


#21- Write a Python program to separate and print the numbers and their position of a
given string.


# In[577]:


def number_sep(string):
    pat='\d+'
    N=re.finditer(pat,string)
    
    for NUM in N:
        print(NUM)


# In[578]:


number_sep("There are 345 people, in which 245 are men, and 100 women.")


# In[ ]:


# 22- Write a regular expression in python program to extract maximum/largest numeric
value from a string.


# In[585]:


SampleText= 'My marks in each semester are 947, 896, 926, 524, 734, 950, 642'
pattern='\d+'
P=re.findall(pattern,SampleText)
print(P)


# In[596]:


P.sort()


# In[597]:


P


# In[600]:


biggest_number=P[-1]
P[-1]


# In[ ]:


#23- Create a function in python to insert spaces between words starting with capital
letters.


# In[607]:


def space (text):
    patt='(?<!\b)(?=[A-Z])'
    print(re.sub(patt," ",text))


# In[608]:


space('ThisIsMyCar.IWillDriveIt.')


# In[ ]:


#24- Python regex to find sequences of one upper case letter followed by lower case letters


# In[623]:


string='s234fTasd45j'
character=re.findall('[A-Z]+[a-z]+',string)
print(character)


# In[ ]:


#25.Write a Python program to remove continuous duplicate words from Sentence using
Regular Expression.


# In[654]:


def remove_duplicate (text):
    pattern=r'\b(\w+)\s+\1+\b'
    print(re.sub(pattern, '\1 ', text))


# In[655]:


remove_duplicate('Hello hello world world')


# In[ ]:


#26- Write a python program using RegEx to accept string ending with alphanumeric
character.


# In[710]:


def world (data):
    p='\w+$'
    print(re.findall(p,data))


# In[713]:


world('His salary is 56k')


# In[ ]:


#27-Write a python program using RegEx to extract the hashtags.


# In[685]:


TEXT= 'RT @kapil_kausik #Doltiwal I mean #xyzabc is hurt&quot by #Demonetization as the same has rendered USELESS lt <ed><U+00AO ><U+00BD><ed><U+00B1><U+0089> "acquired funds" no wo'  
pat=r'[#]+\w+'
str=re.findall(pat,TEXT)
print(str)


# In[ ]:


#28- Write a python program using RegEx to remove <U+..> like symbols


# In[35]:


sample_text='@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders'
pattern='<U[+]\w+>'
result=re.sub(pattern,"",sample_text)
print(result)


# In[ ]:


#29--Write a python program to extract dates from the text stored in the text file.
Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.


# In[8]:


import re
with open ('file2')as FILE:
    B=FILE.read()


# In[13]:


B


# In[14]:


result=re.findall(r'\d+[-]\d+[-]\d+',B)
print(result)


# In[12]:


#30-Create a function in python to remove all words from a string of length between 2 and 4


# In[757]:


def remove_words (string):
    pattern=re.compile(r'\b\w{2,4}\b')
    result=pattern.sub('',string)
    print(result)


# In[758]:


remove_words('The following example creates an ArrayList with a capacity of 50 elements. 4 element are then added to the ArrayList and the ArrayList is trimmed accordingly.')


# In[ ]:





# In[ ]:




