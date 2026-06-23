class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 🐢🐇 Phase 1: Detect cycle (Floyd's Tortoise & Hare)
        slow, fast = 0, 0
        while True:
            slow = nums[slow]              # move slow 1 step
            fast = nums[nums[fast]]        # move fast 2 steps
            if slow == fast:
                break                      # cycle detected

        # 🎯 Phase 2: Find entrance to cycle (duplicate number)
        slow2 = 0
        while True:
            slow = nums[slow]              # move both 1 step
            slow2 = nums[slow2]
            if slow == slow2:
                return slow                # duplicate found
