# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 🟢 Step 1: Find the middle using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 🟠 Step 2: Reverse the second half of the list
        second = slow.next      # Start of second half
        prev = None
        slow.next = None        # Break the list into two halves
        while second:
            tmp = second.next   # Store next node
            second.next = prev  # Reverse the link
            prev = second       # Move prev forward
            second = tmp        # Move second forward

        # 🟣 Step 3: Merge the two halves
        first, second = head, prev  # second is now reversed list head
        while second:
            tmp1, tmp2 = first.next, second.next  # Save next nodes
            first.next = second                   # Point first to second
            second.next = tmp1                    # Link second to next of first
            first, second = tmp1, tmp2            # Move both forward
