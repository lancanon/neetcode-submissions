class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store the word at the end node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # mark the end of a word
        
        rows, cols = len(board), len(board[0])
        result = []

        def backtrack(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            next_node = node.children[char]
            
            # Check if we found a word
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # avoid duplicates
            
            # Mark cell as visited
            board[r][c] = '#'  
            
            # Explore neighbors
            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    backtrack(nr, nc, next_node)
            
            # Restore cell
            board[r][c] = char

        # Start backtracking from each cell
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root)
        
        return result
