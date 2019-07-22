class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = []
        

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for d in dict:
            self.dict.append(d)
        

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        def comp(a,b):
            if len(a)!=len(b):
                return 0
            count = 0
            for w1,w2 in zip(a,b):
                if w1!=w2:
                    count+=1
            return count == 1
        for s in self.dict:
            if comp(s,word):
                return True
        return False
        
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
