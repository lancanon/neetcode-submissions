# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0  # This will store the maximum diameter found so far

        def dfs(root):
            nonlocal res  # so we can modify res inside dfs

            if not root:
                return 0  # If node is None, depth is 0

            # Recursively find depth of left subtree
            left = dfs(root.left)

            # Recursively find depth of right subtree
            right = dfs(root.right)

            # The longest path through this node is left depth + right depth
            # Update res if this path is longer than previous maximum
            res = max(res, left + right)

            # Return the height of the current node (max depth of subtrees + 1)
            return 1 + max(left, right)

        dfs(root)  # Start DFS from root
        return res  # Return the maximum diameter found
