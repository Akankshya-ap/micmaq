
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data=pd.read_csv('/home/apatra/Desktop/work/corpus_edited_sent.txt',sep='\n',header=None)
ts =  data.shape 
print ts
#print data
df=pd.DataFrame(data)


# In[3]:


'''new_train = df.reindex(np.random.permutation(df.index))
print new_train.shape
print new_train[:2764]
indice_70_percent = int((ts[0]/100.0)* 70)

print "70% indice", indice_70_percent

#write train products to csv 
#new_train.to_csv(sep="|")

with open('/home/apatra/Desktop/work/train.txt', 'w') as f:
    for i in new_train[:indice_70_percent][0]:
        #print i
        f.write(str(i)+'\n')


with open('test_products.txt', 'w') as f:
    for i in new_train[indice_90_percent:]:
        f.write(i+'\n')
'''


# In[9]:


print data
df=pd.DataFrame(data)
#print df
div1=np.random.rand(len(df))<0.8 ####80%for training
train=df[div1]
total=df[~div1]
div2=np.random.rand(len(total))<0.5 ####10%for development
develop=total[div2]
test=total[~div2]     ####10%for test



# In[10]:


print train
print type(train)
#train.to_pickle('/home/apatra/Desktop/work/train.txt')

with open('/home/apatra/Desktop/work/train.txt', 'w') as f:
    for i in train[0]:
        #print i
        f.write(str(i))
        f.write('\n')

#np.savetxt(r'/home/apatra/Desktop/work/train.txt',train.values,fmt='%s')
#f0=open('/home/apatra/Desktop/work/train.txt','w')
#f0.writelines(str(train[0]))


# In[14]:


print develop


with open('/home/apatra/Desktop/work/valid.txt', 'w') as f:
    for i in develop[0]:
        #print i
        f.write(str(i))
        f.write('\n')


# In[15]:


print test


with open('/home/apatra/Desktop/work/test.txt', 'w') as f:
    for i in test[0]:
        #print i
        f.write(str(i))
        f.write('\n')


# In[16]:


fv=open('/home/apatra/Desktop/work/valid.txt','r')
for line in fv:
    print line


# Hi Akankshya!
# 
