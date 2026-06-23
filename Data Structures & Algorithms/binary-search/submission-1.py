class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Set left and right pointers to search between
        l, r = 0, len(nums) - 1

        # Keep searching while left pointer is <= right pointer
        while l <= r:
            # Find the middle index (avoids overflow)
            m = l + ((r - l) // 2)

            # If middle value is too big, discard right half
            if nums[m] > target:
                r = m - 1

            # If middle value is too small, discard left half
            elif nums[m] < target:
                l = m + 1

            # Found it!
            else:
                return m

        # If we reach here, target is not in the list
        return -1
