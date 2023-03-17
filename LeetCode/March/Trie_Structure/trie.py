class Trie:

    def __init__(self):
        self.trie_set = []

    def insert(self, word: str) -> None:
        if word not in self.trie_set:
            self.trie_set.append(word)

    def search(self, word: str) -> bool:
        if word in self.trie_set:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        for word in self.trie_set:
            if word.startswith(prefix):
                return True

        return False

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)