# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to simplify appending
        dummy = node = ListNode()

        # Traverse both lists while neither is empty
        while list1 and list2:
            if list1.val < list2.val:
                # list1 has smaller value → add it to merged list
                node.next = list1
                list1 = list1.next
            else:
                # list2 has smaller (or equal) value → add it to merged list
                node.next = list2
                list2 = list2.next
            
            # Move the pointer forward in the merged list
            node = node.next

        # At this point, one of the lists is empty
        # Attach the remaining list (if any)
        node.next = list1 or list2

        # Return the merged list (skip dummy)
        return dummy.next
