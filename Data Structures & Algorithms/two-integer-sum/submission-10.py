class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create a dictionary to store each number and its index
        seen = {}

        # Loop through the list with both index and number
        for i, num in enumerate(nums):
            # Calculate the number we need to reach the target
            diff = target - num

            # Check if we've already seen the needed number
            if diff in seen:
                # If yes, return the index of the needed number and the current index
                return [seen[diff], i]
            # Otherwise, store the current number with its index
            seen[num] = i


        
        