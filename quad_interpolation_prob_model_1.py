from nltk.util import ngrams
from nltk.corpus import stopwords
import nltk
from collections import Counter
from collections import defaultdict

tokens=[]
with open('/home/meghana/nltk_data/corpora/gutenberg/corpusfile.txt') as f:

    for line in f:
        if not line.isspace():
            line=line.lower()
            line=line.replace('.',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('!',' ').replace('?',' ').replace('(',' ').replace(')',' ').replace("-"," ").replace("' ",' ').replace('"',' ').replace("_"," ")
        items=line.split()
        tokens+=items    
tokenSet=set(tokens)

print(len(tokens))
print(len(tokenSet))

bigrams=list(ngrams(tokens,2))
trigrams=list(ngrams(tokens,3))
trigramSet=set(trigrams)
quadgrams=list(ngrams(tokens,4))
quadgramSet=set(quadgrams)

print(len(trigramSet))
print(len(quadgramSet))

unigram_table=Counter(tokens)
bigram_table=Counter(bigrams)
trigram_table=Counter(trigrams)#stores the frequencies of each trigram
quadgram_table=Counter(quadgrams)#stores the frequencies of each quadgram

for key in quadgram_table:
    tri=key[0:3]
    quadgram_table[key]=(quadgram_table[key]/trigram_table[tri])#Now the quadgram table will contain probabilities of each quadgram

for key in trigram_table:
    bi=key[0:2]
    trigram_table[key]=(trigram_table[key]/bigram_table[bi])
for key in bigram_table:
    uni=key[0]
    bigram_table[key]=(bigram_table[key]/unigram_table[uni])
for key in unigram_table:
    n=len(tokens)
    unigram_table[key]=(unigram_table[key]/n)

prob_table = defaultdict(dict)

#Constructing a probabiltity table which looks like this:
#{tri1:{token1:0.2, token5:0.5, tokenn:0.3}
# tri2:{........}
# tri3:{        }
# .....
# trin:{........}}
for quad in quadgram_table:
    p=0.25*(quadgram_table[quad]+trigram_table[quad[0:3]]+bigram_table[quad[0:2]]+unigram_table[quad[0]])
    tri=quad[0:3]
    token=quad[3]
    prob_table[tri][token]=p

for tri in prob_table:
    prob_table[tri]=sorted(prob_table[tri].items(), key=lambda x: x[1], reverse=True)


#s=input("Enter a string:")
s="she is the youngest of"# a sentence in corpus. We need to find the next word for this sentence

s=s.lower()
s=s.replace('.',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('!',' ').replace('?',' ').replace('(',' ').replace(')',' ').replace("' ",' ').replace("-"," ").replace('"',' ').replace("_"," ")                                 
s_tokens=s.split()

s_trigrams=list(ngrams(s_tokens, 3))
#print(s_trigrams)
n=len(s_trigrams)
req_trigram=s_trigrams[n-1]#taking the last trigram to predict the next word

max_prob=0
result='0'
word=prob_table[req_trigram]#word is a list of tokens that are possible to occur after the required trigram

#here it is searching for the token with the highest probability and stores it in result.
# for key,value in word.items():
#     #print(word[key])
#     if(word[key]>max_prob):
#         max_prob=value
#         result=key
print(word)
x=int(input("enter n:"))
n=len(word)
if(x>n):
    n=n
else:
    n=x
result=word[n-1]
#print(result[0])

print("The next word is:", result[0])

#result=' '.join(req_trigram)+" "+result
#print("The sentence might be:", result)