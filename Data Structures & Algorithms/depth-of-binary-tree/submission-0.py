# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Stack holds pairs of [node, current_depth]
        stack = [[root, 1]]
        res = 0  # This will track the max depth found

        while stack:
            node, depth = stack.pop()

            if node:
                # Update max depth if this node's depth is greater
                res = max(res, depth)

                # Push left and right children onto the stack
                # Increase depth by 1 for children
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res
