# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hash map for quick lookup of root index in inorder
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        
        # Pointer to current root in preorder
        self.pre_idx = 0
        
        # Recursive helper to build tree from inorder[left:right]
        def helper(left, right):
            # Base case: no elements to construct subtree
            if left > right:
                return None
            
            # Pick current root from preorder
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            
            # Move preorder pointer to next root
            self.pre_idx += 1
            
            # Build left and right subtrees
            # Left subtree: all nodes in inorder[left : root_index-1]
            root.left = helper(left, inorder_index[root_val] - 1)
            # Right subtree: all nodes in inorder[root_index+1 : right]
            root.right = helper(inorder_index[root_val] + 1, right)
            
            return root
        
        # Build the whole tree from inorder[0 : len-1]
        return helper(0, len(inorder) - 1)
