# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 🟢 Dummy node simplifies edge cases (like removing the first node)
        dummy = ListNode(0, head)

        # 🟠 Set two pointers
        left = dummy
        right = head

        # Move the right pointer n steps ahead
        while n > 0:
            right = right.next
            n -= 1

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Now, left is just before the node to remove
        left.next = left.next.next

        # Return the actual head (skip dummy)
        return dummy.next
