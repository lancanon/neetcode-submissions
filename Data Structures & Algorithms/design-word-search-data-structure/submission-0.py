class TrieNode:
    def __init__(self):
        # Children nodes: char -> TrieNode
        self.children = {}
        # True if this node marks the end of a word
        self.is_end = False

class WordDictionary:
    def __init__(self):
        # Root node of the Trie
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            # If character not in children, create a new TrieNode
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Mark the end of the word
        node.is_end = True

    def search(self, word: str) -> bool:
        # Helper function to search recursively
        def dfs(node, i):
            # Base case: reached end of word
            if i == len(word):
                return node.is_end

            char = word[i]

            if char == '.':
                # '.' can match any character → try all children
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # Normal character → must follow that path
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)

        # Start DFS from root at index 0
        return dfs(self.root, 0)
