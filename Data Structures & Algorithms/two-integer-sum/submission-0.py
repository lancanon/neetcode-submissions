class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # aka "hash map" or "dictionary" to store numbers and their indices
        
        # First pass: Build the hash map with all numbers and their indices
        for i, n in enumerate(nums):  
            indices[n] = i  # Store the number as the key and its index as the value
        
        # Second pass: Check for the complement (target - current number)
        for i, n in enumerate(nums):  
            diff = target - n  # Find the number we need to pair with 'n' to get the target
            
            # Check if the complement exists in the hash map and isn't the same number
            if diff in indices and indices[diff] != i:  
                return [i, indices[diff]]  # Return the indices of the pair
