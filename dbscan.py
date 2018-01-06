
# coding: utf-8

# In[38]:


from sklearn.cluster import DBSCAN
import string
from gensim.models import Word2Vec


# In[39]:


x=[]
with open("labels.txt") as lines:
    for line in lines:
        x.append(line.strip().translate(string.punctuation))


# In[40]:


#import 
from os import path
import string
import os
import re
import pandas as pd
import numpy as np
import gensim
from gensim.models import word2vec

model = gensim.models.Word2Vec.load('model50.model')

#df = pd.DataFrame()


num_features=50


def sentvec(sent,m=num_features,model=model): 
    res = np.zeros(m) 
    words = sent.split() 
    num = 0  
    for w in words: 
        if w in model.wv.index2word: 
            res += model[w] 
            num += 1.0 
    if num == 0: return np.zeros(m) 
    else: return res/num 
     
#n = df.shape[0] 


"""
for i ,sent in enumerate(df.seg_word.values): 
    sent_matrix[i,:] = sentvec(sent) 
print(sent_matrix.shape)
"""

f = open("labels.txt","r")  
lines = f.readlines()#读取全部内容  
f.close()
for i in range(0,len(lines),1):
    lines[i]=lines[i].replace('\n',"")
#print(lines[0:10])

sent_matrix = np.zeros([len(lines),num_features],float) 

for k in range(0,len(lines),1):
    sent_matrix[k,:] = sentvec(lines[k]) 
print(sent_matrix.shape)
print(sent_matrix)


# In[41]:


import matplotlib as plt
#y_pred = DBSCAN(eps = 0.05, min_samples = 10).fit_predict(sent_matrix)
#y = DBSCAN(eps = 0.1, min_samples = 10).fit(sent_matrix)
#print(y_pred)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=10, random_state=0).fit(sent_matrix)
print(kmeans.labels_)
print(kmeans.cluster_centers_)


# In[34]:


result=y_pred.tolist()
res_dic={k: v for k, v in enumerate(result)}


# In[35]:


res_0=[]
res_1=[]
res_2=[]
res_3=[]
res_4=[]
res_5=[]
res_6=[]
res_7=[]
res_8=[]
res_9=[]
res_10=[]
res_11=[]

for key, value in res_dic.items():
    if(value==0): res_0.append(key)
    if(value==1): res_1.append(key)
    if(value==2): res_2.append(key)
    if(value==3): res_3.append(key)
    if(value==4): res_4.append(key)
    if(value==5): res_5.append(key)
    if(value==6): res_6.append(key)
    if(value==7): res_7.append(key)
    if(value==8): res_8.append(key)
    if(value==9): res_9.append(key)
    if(value==10): res_10.append(key)
    if(value==11): res_11.append(key)


# In[37]:


print(result)


# In[25]:


file = open('labels.txt', 'w')
for item in resl_0:
    file.write("%s\n" % item)


# In[ ]:


# get the label nearest center cluster 

