from nltk.util import ngrams
from nltk.corpus import stopwords
import nltk
from collections import Counter
from collections import defaultdict
import os


class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
        self.eq = None
class TST:
    def __init__(self):
        self.root = Node()
        self.leaf = None

    @staticmethod
    def _search(node, leaf):
        while node:
            if node.data == leaf:
                return node
            if str(leaf) < str(node.data):
                node = node.left
            else:
                node = node.right
        return None

    def _insert(self, node, leaf):
        if node is None:
            return leaf
        elif leaf.data == node.data:
            return node
        elif str(leaf.data) < str(node.data):
            node.left = self._insert(node.left, leaf)
        else:
            node.right = self._insert(node.right, leaf)
        return node

    def insert(self, quad):
        node = self.root
        for word in quad:
            #print(char)
            child = self._search(node.eq, word)
            if not child:  # not null
                # create a new node
                child = Node(word)
                node.eq = self._insert(node.eq, child)
            node = child
        if not self._search(node.eq, self.leaf):  # not null
            node.eq = self._insert(node.eq, Node(self.leaf))

    def search(self, word):
        node = self.root
        for c in word:
            node = self._search(node.eq, c)
            if not node:
                return False
        return self._search(node.eq, self.leaf) is not None

    def _traverse(self, node, leaf):
        if node:
            for c in self._traverse(node.left, leaf):
                yield c

            if node.data == leaf:
                #print([])
                yield []
            else:
                for c in self._traverse(node.eq, leaf):
                    #print(c)
                    yield [node.data] + c
            for c in self._traverse(node.right, leaf):
                yield c

    def traverse(self):
        for w in self._traverse(self.root.eq, self.leaf):
            print(''.join(w))

    def common_prefix(self, chars):
        node = self.root
        buff = []
        for word in chars:
            buff.append(word)
            print(buff)
            node = self._search(node.eq, word)
            if not node:
                return
        for x in self._traverse(node.eq, self.leaf):
            print(x)
            yield ' '.join(x)
            #yield ''.join(buff + x)


if __name__ == '__main__':
    
    # tst = TST()
    # names = ['arun', 'ari', 'aari', 'aruna']
    # for name in names:
    #     tst.insert(name)
    # print(tst.search('nithya'))
    # print(tst.search('aari'))
    # tst.traverse()
    
    # tst = TST()
    # with open('sample_text.txt', 'r+') as dictionary:
    #     for entry in dictionary.readlines():
    #         tst.insert(entry)
    # for item in tst.common_prefix('meghan is a'):
    #     print(item)
    tokens=[]
    #with open('/home/meghana/new_jupyter/assign1/Data/Tokenization/Chat1.txt') as f:
    with open('/home/meghana/nltk_data/corpora/gutenberg/corpusfile.txt') as f:

        for line in f:
            if not line.isspace():
                line=line.lower()
                line=line.replace('.',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('!',' ').replace('?',' ').replace('(',' ').replace(')',' ').replace("-"," ").replace("' ",' ').replace('"',' ').replace("_"," ").replace('[',' ').replace(']',' ')
            items=line.split()
            tokens+=items    
    tokenSet=set(tokens)

    print(len(tokens))
    print(len(tokenSet))

    #trigrams=list(ngrams(tokens,3))
    #trigramSet=set(trigrams)
    quadgrams=list(ngrams(tokens,4))
    quadgramSet=set(quadgrams[0:20])

    fh=open('quad.txt','w')
    for quad in quadgramSet:
        line=str(quad)
        line=line.lower()
        line=line.replace(',','').replace('(','').replace(')','').replace("'",'').replace('"','')
        fh.write(str(line)+ os.linesep)
    fh.close()

    

    tst = TST()
    with open('quad.txt', 'r+') as dictionary:
        for entry in dictionary.readlines():
            #print(entry)
            tst.insert(entry)
    # for item in tst.common_prefix('emma'):
    #     print(item)
    x=list(tst.common_prefix('emma by jane'))
    #print(type(x))
    #for word in x:
    print(x)
    
    # tst=TST()
    # for quad in quadgrams[0:20]:
    #     tst.insert(quad)
    # for item in tst.common_prefix(''):
    #     print(item)
