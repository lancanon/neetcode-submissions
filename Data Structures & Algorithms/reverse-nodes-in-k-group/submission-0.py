# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Dummy node before head
        groupPrev = dummy          # Used to connect reversed groups

        while True:
            # 🧭 Step 1: Get the kth node ahead
            kth = self.getKth(groupPrev, k)
            if not kth:
                break  # Not enough nodes left to reverse

            groupNext = kth.next  # Save the next group's head

            # 🔄 Step 2: Reverse this k-group
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # 🔗 Step 3: Reconnect reversed group to main list
            tmp = groupPrev.next        # store current group's head (will become tail)
            groupPrev.next = kth        # kth is new head of reversed group
            groupPrev = tmp             # move to next group's previous

        return dummy.next  # dummy.next is the new head

    # Helper to get the kth node from curr
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
