# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None  # Base case: empty list → return None

        newHead = head
        if head.next:
            # Recursively reverse the rest of the list
            newHead = self.reverseList(head.next)
            
            # Reverse the current pointer: head.next is the "next node"
            # So its .next should point back to the current node (head)
            head.next.next = head
        
        # Disconnect the current node from the rest to avoid cycle
        head.next = None

        return newHead  # Always return the new head from recursion
