class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        print(f"Input list: {nums}")

        for n in nums:
            print(f"Checking: {n}")
            if n in seen:
                print(f"Duplicate found: {n}")
                return True
            print(f"Adding {n} to seen set.")
            seen.add(n)
        
        print("No duplicates found.")
        return False
