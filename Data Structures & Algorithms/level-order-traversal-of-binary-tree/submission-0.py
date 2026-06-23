
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:  # edge case: empty tree
            return []

        res = []
        queue = deque([root])  # initialize queue with root

        while queue:
            level = []
            level_size = len(queue)  # number of nodes in current level

            for _ in range(level_size):
                node = queue.popleft()   # pop from queue
                level.append(node.val)   # add value to current level
                if node.left:
                    queue.append(node.left)   # add left child
                if node.right:
                    queue.append(node.right)  # add right child

            res.append(level)  # add this level's result

        return res
