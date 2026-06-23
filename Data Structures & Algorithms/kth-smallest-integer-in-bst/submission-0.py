# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize a counter for how many nodes we've visited
        self.cnt = 0
        # Initialize a variable to store the k-th smallest value once we find it
        self.res = None

        # Define the in-order traversal function (DFS)
        def inorder(node):
            if not node or self.res is not None:  # base case: empty node or already found
                return

            # 1. Visit the left subtree first (smaller values in BST)
            inorder(node.left)

            # 2. Visit current node
            self.cnt += 1               # increment the counter
            if self.cnt == k:           # if we've reached the k-th node
                self.res = node.val     # store its value as the answer
                return                   # stop further traversal

            # 3. Visit the right subtree next (larger values in BST)
            inorder(node.right)

        # Start in-order traversal from the root
        inorder(root)

        # Return the k-th smallest value
        return self.res
