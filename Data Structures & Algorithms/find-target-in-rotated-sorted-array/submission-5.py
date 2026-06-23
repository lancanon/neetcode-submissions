class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1: Find the pivot (smallest element's index)
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            # If mid element is greater than rightmost element,
            # that means the smallest is to the right of mid
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m  # Smallest is at mid or to the left of mid

        pivot = l  # The index of the smallest element (rotation point)

        # Step 2: Decide which side of the pivot to do binary search on
        l, r = 0, len(nums) - 1

        # If target is in the range from pivot to end of array
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot  # Search in the right half
        else:
            r = pivot - 1  # Search in the left half

        # Step 3: Standard binary search in the chosen half
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m  # Target found
            elif nums[m] < target:
                l = m + 1  # Move right
            else:
                r = m - 1  # Move left

        return -1  # Target not found

