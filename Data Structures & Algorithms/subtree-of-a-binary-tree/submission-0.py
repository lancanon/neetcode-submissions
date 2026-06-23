# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case: empty subtree is always a subtree
        if not subRoot:
            return True

        # If main tree is empty but subtree isn't, can't be a subtree
        if not root:
            return False

        # If current node trees are identical, return True
        if self.sameTree(root, subRoot):
            return True

        # Otherwise, check if subRoot is a subtree of left or right subtree of root
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Both trees empty → same
        if not root and not subRoot:
            return True

        # Both nodes exist and have same value
        if root and subRoot and root.val == subRoot.val:
            # Recursively check left and right subtrees
            return (self.sameTree(root.left, subRoot.left) and 
                    self.sameTree(root.right, subRoot.right))

        # Otherwise, trees differ
        return False
