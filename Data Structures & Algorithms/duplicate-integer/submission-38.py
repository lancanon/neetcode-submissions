class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

sol = Solution()

print(sol.hasDuplicate([1,2,3,4]))
print(sol.hasDuplicate([1,2,3,4]))
print(sol.hasDuplicate([1,2,2,2]))
        