class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a hashset
        seen = set()
        #for a value in the list
        #if the value is in seen return True (duplicate)
        #else add the value to the hashset, end the for loop
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        