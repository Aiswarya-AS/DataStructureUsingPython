class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.endOfWord = True

    def search(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.endOfWord

    def startsWith(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True

    def _find_words(self, node):
        result = []
        if node.endOfWord:
            result.append("")
        for char, child in node.children.items():
            suffixes = self._find_words(child)
            for suffix in suffixes:
                result.append(char + suffix)
        return result


t = Trie()
t.insert("apple")
t.insert("pineapple")
c = t.search("apple")
print(c)
s = t.startsWith("zeb")
print(s)
