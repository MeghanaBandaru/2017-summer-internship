class Node(object):

    def __init__(self,word):
        self.word=word
        self.left=None
        self.eq=None
        self.right=None

class TST(object):
    
    def __init__(self):
        self.root=None
    
    def put(self, quad, freq):

        self.root=self.putItem(self.root, quad, freq, 0);

    def putItem(self, node, quad, freq, index):

        token=quad[index]
        #print(token)

        if node==None:
            node=Node(token)

        if token<node.word:
            node.left=self.putItem(node.left,quad,freq,index)
        elif token>node.word:
            node.right=self.putItem(node.right,quad,freq,index)
        elif index<len(quad)-1:
            node.eq=self.putItem(node.eq,quad,freq,index+1)
        else:
            node.freq=freq
        return node

    def searchItem(self,node,words):
        if node==None:
            return
        words.append(node.word)

        if node.left==None and node.right==None:
            self.printWords(words)
        else:
            self.searchItem(node.left,words)
            self.searchItem(node.right,words)

    def printWords(self,words):

        #words=self.searchItem(node,words)
        #for i in wordLength:
        print(words)           

    def get(self,tri):
        node=self.getItem(self.root, tri, 0)
        print(node.word)

        if node==None:
            return None
        #return node.word,node.freq;
        words=[]
        self.searchItem(node,words)
        #self.printWords(node,words)
    

    #to find the node where the trigram ends
    def getItem(self,node,tri,index):

        if node==None:
            return None
        token=tri[index]

        if token<node.word:
            return self.getItem(node.left,tri,index)
        elif token>node.word:
            return self.getItem(node.right,tri,index)
        elif index<len(tri)-1:
            return self.getItem(node.eq,tri,index+1)
        else:
            return node.eq
    

    # To search the whole quadgram:-
    def findItem(self,node,quad,index):

      if node==None:
          return None
      token=quad[index]
      #print(token)
        
      if token<node.word:
          return self.findItem(node.left,quad,index)
      elif token>node.word:
          return self.findItem(node.right,quad,index)
      elif index<len(quad)-1:
          return self.findItem(node.eq,quad,index+1)
      else:
          return node;

    def searchQuad(self,quad):
        node=self.findItem(self.root,quad,0)

        if node==None:
            return None
        return node.word

    

# if __name__ == '__main__':
#   tst=TST()

#   tst.put("apple",100)
#   tst.put("orange",200)

#   print(tst.get("apple"))



