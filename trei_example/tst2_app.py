from tst2 import Node
from tst2 import TST 

from nltk.util import ngrams
from nltk.corpus import stopwords
import nltk
from collections import Counter
from collections import defaultdict
import os

tokens=[]
#with open('/home/meghana/new_jupyter/assign1/Data/Tokenization/Chat1.txt') as f:
with open('/home/meghana/nltk_data/corpora/gutenberg/corpusfile.txt') as f:

    for line in f:
        if not line.isspace():
            line=line.lower()
            line=line.replace('.',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('!',' ').replace('?',' ').replace('(',' ').replace(')',' ').replace("-"," ").replace("' ",' ').replace('"',' ').replace("_"," ").replace('[',' ').replace(']',' ')
        items=line.split()
        tokens+=items    
#tokenSet=set(tokens)


quadgrams=list(ngrams(tokens,4))
#quadgrams.append(('emma', 'by', 'jane','potter'))
#quadgramSet=set(quadgrams[0:20])
#quadgrams=quadgrams[0]
#quadgrams.append(('emma', 'by', 'jane','potter'))
quadgram_table=Counter(quadgrams)

tst=TST()

for quad in quadgram_table:
	#print(quad,quadgram_table[quad])
	tst.put(quad,quadgram_table[quad])
print("done")
x=('she', 'is', 'the')
# w,f=tst.get(x)
# print(w,f)
tst.get(x)
print("done")
# w=list(w)
# print(w)

# y=('emma', 'by', 'jane','potter')
# w=tst.searchQuad(y)
# print(w)