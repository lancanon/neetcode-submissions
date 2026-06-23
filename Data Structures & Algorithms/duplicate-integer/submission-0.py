class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a set to store unique numbers
        seen = set()
        
        # Iterate through the array
        for num in nums:
            # If the number is already in the set, return True
            if num in seen:
                return True
            # Otherwise, add the number to the set
            seen.add(num)
        
        # If no duplicates are found, return False
        return False