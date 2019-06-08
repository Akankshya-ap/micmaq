
# coding: utf-8

# In[1]:


fil=[]
doc=[]
par=[]
sent=[]
lines=''
k=0
####sentence_wise
f0=open('/home/apatra/Desktop/work/corpus_edited_sent.txt','w')
#####paragraph_wise
f1=open('/home/apatra/Desktop/work/corpus_edited_par.txt','w')
#####document_wise
f2=open('/home/apatra/Desktop/work/corpus_edited_doc.txt','w')
with open('/home/apatra/Desktop/work/corpus_micmac_cleanponctuation.txt') as f4:
    for line in f4:   

        if '</s>' in line:
            #print "hi"
            k=0
            print lines
            f0.write(lines)
            f0.write("\n")
            par.append(lines)
            lines=''
        if k==1:
            if '\r\n' or '\n' in line:
                #print "hi"
                #print line
                line=line.replace("\r\n"," ")
            lines+=line
        if '<s>' in line:
            #print "hi"
            k=1

        if '</p>' in line:
            f1.write(str(par))
            f1.write("\n")
            doc.append(par)
            #print doc
            par=[]
        if '</doc>' in line:
            f2.write(str(doc))
            f2.write("\n")
            fil.append(doc)
            #print fil
            doc=[]
    #print len(fil)
    #print fil


# In[2]:


f0.close()
f1.close()
f2.close()


# In[3]:


###number of documents
print len(fil)


# In[4]:


f0=open('/home/apatra/Desktop/work/corpus_edited_sent.txt','r')

x0=f0.read()
#####number of tokens
print len(x0.split())


# In[5]:


#####number of types
print(len(set(x0.split())))

