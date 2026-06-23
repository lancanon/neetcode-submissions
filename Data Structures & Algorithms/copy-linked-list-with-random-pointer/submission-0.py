"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Dictionary that maps original node -> copied node
        oldToCopy = {None: None}

        # 🟢 First pass: create all nodes (without connecting them)
        cur = head
        while cur:
            copy = Node(cur.val)     # Make a copy
            oldToCopy[cur] = copy   # Save mapping
            cur = cur.next

        # 🔵 Second pass: assign .next and .random using saved map
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]  # Return the deep copied head