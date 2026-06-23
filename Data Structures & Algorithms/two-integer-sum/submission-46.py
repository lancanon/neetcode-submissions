class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #create a dict to store an array of integers
        seen = {}

        for i,num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff],i]
                
            seen[num] = i
            
        