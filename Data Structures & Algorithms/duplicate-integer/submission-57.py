class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # {1,4,5,6,7,8}
        # (1, 3,4,4)

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False



        