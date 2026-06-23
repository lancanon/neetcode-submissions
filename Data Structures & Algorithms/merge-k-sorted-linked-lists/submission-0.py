# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case: if input is empty or all None
        if not lists or len(lists) == 0:
            return None

        # Merge lists two at a time until one is left
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                # Get two lists to merge
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # Merge and add to new list
                mergedLists.append(self.mergeList(l1, l2))
            # Update original list to merged list for next round
            lists = mergedLists

        return lists[0]  # Only one list remains

    def mergeList(self, l1, l2):
        dummy = ListNode()  # Dummy node to simplify result creation
        tail = dummy

        # Merge two sorted lists
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach remaining nodes
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next  # Skip dummy and return real head
