
# coding: utf-8

# In[ ]:


import numpy as np
import codecs
class FastVector:
    """
    Minimal wrapper for fastvector embeddings.
    ```
    Usage:
        $ model = FastVector(vector_file='/path/to/wiki.en.vec')
        $ 'apple' in model
        > TRUE
        $ model['apple'].shape
        > (300,)
    ```
    """

    def __init__(self, vector_file='', transform=None):
        """Read in word vectors in fasttext format"""
        self.word2id = {}

        # Captures word order, for export() and translate methods
        self.id2word = []

        print('reading word vectors from %s' % vector_file)
        with open(vector_file, 'r') as f:
	    print ('1') 
            (self.n_words, self.n_dim) =             (int(x) for x in f.readline().rstrip('\n').split(' '))
            self.embed = np.zeros((self.n_words, self.n_dim))
            for i, line in enumerate(f):
                elems = line.rstrip('\n').split(' ')
                self.word2id[elems[0]] = i
                #print (elems[0])
                self.embed[i] = elems[1:self.n_dim+1]
                self.id2word.append(elems[0])
        
        # Used in translate_inverted_softmax()
        self.softmax_denominators = None
        
        if transform is not None:
            print('Applying transformation to embedding')
            self.apply_transform(transform)
    
    def apply_cop(self, matrix,i):
        self.embed[i]=matrix[:]
    
    def export(self, outpath):
        """
        Transforming a large matrix of WordVectors is expensive. 
        This method lets you write the transformed matrix back to a file for future use
        :param The path to the output file to be written 
        """
        fout = open(outpath, "w")

        # Header takes the guesswork out of loading by recording how many lines, vector dims
        fout.write(str(self.n_words) + " " + str(self.n_dim) + "\n")
        for token in self.id2word:
            vector_components = ["%.6f" % number for number in self[token]]
            vector_as_string = " ".join(vector_components)

            out_line = token + " " + vector_as_string + "\n"
            fout.write(out_line)

        fout.close()
    
    
    @classmethod
    def cosine_similarity(cls, vec_a, vec_b):
        """Compute cosine similarity between vec_a and vec_b"""
        return np.dot(vec_a, vec_b) /             (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))

    def __contains__(self, key):
        return key in self.word2id

    def __getitem__(self, key):
        return self.embed[self.word2id[key]]


# In[ ]:


import numpy as np
from random import randint


# In[ ]:


def make_training_matrices(source_dictionary, target_dictionary, bilingual_dictionary):
    """
    Source and target dictionaries are the FastVector objects of
    source/target languages. bilingual_dictionary is a list of 
    translation pair tuples [(source_word, target_word), ...].
    """
    source_matrix = []
    target_matrix = []
    ti=[]
    count=0
    for (source, target) in bilingual_dictionary:
        #print source,target
        if source in source_dictionary and target in target_dictionary:
            #print source, target
            count=count+1
            #print source, target
            #print source+1
            x=randint(0,len(source_dictionary.word2id))

            #print x
            source1= source_dictionary.id2word[x]
            print source, source1,target
            ti.append(target_dictionary.word2id[target])
            source_matrix.append(source_dictionary[source1])
            target_matrix.append(target_dictionary[target])
        
    # return training matrices
    print count
    return np.array(source_matrix), np.array(target_matrix), np.array(ti)


# In[ ]:


en_dictionary = FastVector(vector_file='/home/apatra/fastText/fastText_multilingual-master/eng.vec')
mi_dictionary = FastVector(vector_file='/home/apatra/fastText/fastText_multilingual-master/model.vec')

en_vector = en_dictionary["one"]
mi_vector = mi_dictionary["newt"]
print(FastVector.cosine_similarity(en_vector, mi_vector))


# In[ ]:


mi_words = set(mi_dictionary.word2id.keys())
en_words = set(en_dictionary.word2id.keys())


# In[ ]:


import codecs
bilingual_dictionary=[]
with codecs.open('/home/apatra/fastText/fastText_multilingual-master/eng-mic','r','utf-8') as f:
    for line in f:
        eng, mic=line.split(', ')
        #print eng
        eng=eng.strip('\"')
        #print eng
        mic=mic.strip('\"')
        mic=mic.replace('\n','')
        mic=mic.replace('"','')
        #print eng, mic
        bilingual_dictionary.append((eng,mic))
#print bilingual_dictionary


# In[ ]:


# form the training matrices
#from copy import deepcopy
source_matrix, target_matrix ,ti= make_training_matrices(
    en_dictionary, mi_dictionary, bilingual_dictionary)
#print len(source_matrix), len(target_matrix)
# learn and apply the transformation
#print ti, len(ti)
#target_matrix=deepcopy(source_matrix)
#print source_matrix #[60][9], target_matrix[60][9]
#transform = learn_transformation(source_matrix, target_matrix)
#print type(transform)
#print transform[299]
#en_dictionary.apply_transform(transform)


# In[ ]:


from collections import defaultdict

def list_duplicates(seq, x):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return (locs for key,locs in tally.items() 
            if key==x)

'''
ind=6
p=list_duplicates(ti,ti[ind])
#for l in p:
 #   print l
j=np.zeros(300)
print source_matrix[ind]
print source_matrix[191]
for l in p:
    for x in l:
        j+=source_matrix[x]
            
    target_matrix[ind]=j[:]/len(l)
print target_matrix[ind]
'''


# In[ ]:


import copy
count_no=0
j=np.zeros(300)
for r in range(0,len(ti)):
    #print source_matrix[r], target_matrix[r]
    #print len(source_matrix[r]),len(target_matrix[r])
    print ti[r]
    p=list_duplicates(ti,ti[r])
    #print p
    j=np.zeros(300)
    for l in p:
        print l
        for x in l:
            j+=source_matrix[x]
            
        target_matrix[r]=j[:]/len(l)
    count_no+=1
    #target_matrix[r]=source_matrix[r][:]
    mi_dictionary.apply_cop(target_matrix[r],ti[r])
print count_no


# In[ ]:


mi_dictionary.export('/home/apatra/fastText/fastText_multilingual-master/micmaq4.vec')


# In[ ]:


'''for i in range (0,len(bilingual_dictionary)):
    print bilingual_dictionary[i]'''


# In[ ]:


'''from random import randint
x=randint(0,len(en_dictionary.word2id))

print x
print en_dictionary.id2word[x]'''


# In[ ]:


'''print len(en_dictionary.word2id)'''

