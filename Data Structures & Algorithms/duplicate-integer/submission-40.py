class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #stores elements we've alr seen
        seen = set() 

        # for a value in the list if in the hashset, do nothing return true else add it to hashset
        for num  in nums:
            if num in seen:
                return True
            seen.add(num)
        return False