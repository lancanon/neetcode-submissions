# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers at the head
        slow, fast = head, head

        # Move fast by 2 steps and slow by 1 step each time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If they ever meet, there's a cycle
            if slow == fast:
                return True

        # If fast reaches the end, no cycle exists
        return False
