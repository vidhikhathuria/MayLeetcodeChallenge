# Problem Link: https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for i in word:
            root = root.setdefault(i, {})
        root['*'] = '*'
                
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for i in word:
            if i in root:
                root = root[i]
            else:
                return False
        if '*' in root:
            return True
        else:
            return False
        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for i in prefix:
            if i in root:
                root = root[i]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)