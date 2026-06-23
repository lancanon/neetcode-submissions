# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            # If both p and q are greater than current node, LCA must be in right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            
            # If both p and q are less than current node, LCA must be in left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            # Otherwise, current node is split point where p and q diverge
            else:
                return cur
