class TrieNode:
    def __init__(self):
        # Dictionary to store children nodes: char -> TrieNode
        self.children = {}
        # True if this node marks the end of a word
        self.is_end = False

class PrefixTree:
    def __init__(self):
        # Root node does not store any character
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # If the character is not already a child, create a new TrieNode
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        # Mark the end of the word
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            # If the character path does not exist, word is not in Trie
            if char not in node.children:
                return False
            node = node.children[char]
        # Return True only if this node marks the end of a word
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            # If the character path does not exist, no word starts with this prefix
            if char not in node.children:
                return False
            node = node.children[char]
        # All characters in prefix found
        return True
