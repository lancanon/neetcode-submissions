class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to keep track of numbers we've seen
        seen = set()

        # Loop through each number in the list
        for num in nums:
            # If the number is already in the set, we found a duplicate!
            if num in seen:
                return True
            
            # Otherwise, add the number to the set
            seen.add(num)
        
        # If we go through the whole list without finding a duplicate, return False
        return False
