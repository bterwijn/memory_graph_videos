import memory_graph as mg # see install: https://pypi.org/project/memory-graph/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

    def complete_rec(self, word, comp, completions):
        if self.word_end:
            completions.append(word+comp)
        for c, curr in self.children.items():
            curr.complete_rec(word, comp+c, completions)
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word_end = True
        
    def complete(self, word):
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return []
        completions = []
        curr.complete_rec(word, '', completions)
        return completions
    
trie = Trie()
for word in ['cat', 'car', 'care', 'can', 'caps', 'cup', 'cut', 'dog']:
    trie.insert(word)

completions = trie.complete('ca')
print(completions)
mg.sl() # show local variables
