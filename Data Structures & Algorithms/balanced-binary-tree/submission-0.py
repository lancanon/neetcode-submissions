# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]  # Base case: empty tree is balanced with height 0

            left = dfs(root.left)   # Recursively check left subtree, returns [balanced, height]
            right = dfs(root.right) # Recursively check right subtree, returns [balanced, height]

            # balanced if:
            # 1. left subtree is balanced
            # 2. right subtree is balanced
            # 3. height difference between left and right is at most 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # height of current node = 1 + max height of left or right subtree
            height = 1 + max(left[1], right[1])

            return [balanced, height]

        # The answer is whether the entire tree is balanced, which is dfs(root)[0]
        return dfs(root)[0]
