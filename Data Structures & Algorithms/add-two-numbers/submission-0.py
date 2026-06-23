# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   # Dummy node to simplify result building
        cur = dummy          # Pointer to build the new list

        carry = 0            # Carry for addition
        while l1 or l2 or carry:
            # Get values from nodes or use 0 if one list is shorter
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Add digits + carry from previous operation
            val = v1 + v2 + carry
            carry = val // 10        # Extract carry (if val >= 10)
            val = val % 10           # Current digit to store

            # Create new node with the digit
            cur.next = ListNode(val)

            # Move all pointers forward
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Final result starts at dummy.next
        return dummy.next
