
# coding: utf-8

# In[47]:


import pandas as pd
from gensim.models import Word2Vec
import string
import nltk
from nltk.corpus import stopwords
from string import digits


# In[48]:


#load input 
train_data = pd.read_csv('finalfinal.txt',sep='\t',names=['text'])


# In[49]:


#remove punctuations, and lower letters 
translator = str.maketrans('', '', string.punctuation)
remove_digits = str.maketrans('', '', digits)
for i in range(len(train_data['text'])):
    train_data['text'][i] = train_data['text'][i].translate(translator)
    train_data['text'][i] = train_data['text'][i].translate(remove_digits)
    train_data['text'][i] = train_data['text'][i].lower()


# In[50]:


#tokenize train_data
token_res=[]
for i in range(len(train_data['text'])):
    token_res.extend(nltk.word_tokenize(train_data['text'][i]))


# In[51]:


#filter stopwords
filtered_words = [word for word in token_res if word not in stopwords.words('english')]


# In[52]:


#remove all characters except letters
def letters(input):
    return ''.join(filter(str.isalpha, input))
for word in filtered_words:
    word=letters(word)


# In[53]:


#remove string length<2
filtered_words = [word for word in filtered_words if len(word)>1]


# In[54]:


print(filtered_words[1:300])


# In[55]:


#train word2vec on train_data
model50 = Word2Vec(filtered_words, size=50, window=5, min_count=5, workers=2)


# In[56]:


model50.save('model50.model')

