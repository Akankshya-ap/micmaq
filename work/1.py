
# coding: utf-8

# In[171]:


import re
import nltk
f1=open('/home/apatra/Desktop/work/corpus_micmac_cleanponctuation.txt','r')
x1=f1.read()
print (x1)


# In[172]:


print len(x1)
#print sum(1 for '\n' in x)


# In[173]:


doc=re.findall(r'<doc>',x1)
print len(doc)


# In[174]:


import csv
import itertools


# In[199]:


x2=x1.replace("\n"," ")
f2=open('/home/apatra/Desktop/work/corpus_edited.txt','w')
f2.write(x2)
f2.close()


# In[200]:


f3=open('/home/apatra/Desktop/work/corpus_edited.txt','r').read()


# In[201]:


p1=re.search(r'<s.*s\>',f3).group()
print p1


# In[208]:


f2=open('/home/apatra/Desktop/work/corpus2.txt','r')
x2=f2.read()
#print x2
x3=x2.replace("\n"," ")
fo=open('/home/apatra/Desktop/work/corpus2_edited.txt','w')
fo.write(x3)
#print x3


# In[222]:


fo=open('/home/apatra/Desktop/work/corpus2_edited.txt','r')
xo=fo.read()
p1=re.search(r'<s.*/s>',xo).group()
print p1


# In[245]:


import itertools as it
doc=[]
par=[]
sent=[]
lines=''
k=0
with open('/home/apatra/Desktop/work/corpus2.txt') as f4:
    for line in f4:
        if '</s' in line:
            k=0
            print lines
            sent.append(lines)
            lines=''
        if k==1:
            line.replace("\n"," ")
            lines+=line
        if '<s>' in line:
            k=1
        
        
    '''
    if line=='<s>' and sent:
        ''.join(sent)
        sent=[]
    else:
        sent.append(sent)
    print sent
    '''

